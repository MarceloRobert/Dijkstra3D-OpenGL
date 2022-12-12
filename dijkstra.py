#!/usr/bin/env python3

## @file phong.py
#  Applies the Phong method.
# 
# @author Ricardo Dutra da Silva


import sys
import ctypes
import numpy as np
import OpenGL.GL as gl
import OpenGL.GLUT as glut
import utils as ut
from ctypes import c_void_p

import objects as myobj
import graph as mygraph


## Window width.
win_width  = 600
## Window height.
win_height = 600

## Program variable.
program = None
## Vertex array object.
VAO = None
## Vertex buffer object.
VBO = None

## Vertex shader.
vertex_code = """
#version 330 core
layout (location = 0) in vec3 position;
layout (location = 1) in vec3 normal;

uniform mat4 model;
uniform mat4 view;
uniform mat4 projection;

out vec3 vNormal;
out vec3 fragPosition;

void main()
{
    gl_Position = projection * view * model * vec4(position, 1.0);
    vNormal = mat3(transpose(inverse(model)))*normal;
    fragPosition = vec3(model * vec4(position, 1.0));
}
"""

## Fragment shader.
fragment_code = """
#version 330 core
in vec3 vNormal;
in vec3 fragPosition;

out vec4 fragColor;

uniform vec3 objectColor;
uniform vec3 lightColor;
uniform vec3 lightPosition;
uniform vec3 cameraPosition;

void main()
{
    float ka = 0.5;
    vec3 ambient = ka * lightColor;

    float kd = 0.8;
    vec3 n = normalize(vNormal);
    vec3 l = normalize(lightPosition - fragPosition);
    
    float diff = max(dot(n,l), 0.0);
    vec3 diffuse = kd * diff * lightColor;

    float ks = 1.0;
    vec3 v = normalize(cameraPosition - fragPosition);
    vec3 r = reflect(-l, n);

    float spec = pow(max(dot(v, r), 0.0), 3.0);
    vec3 specular = ks * spec * lightColor;

    vec3 light = (ambient + diffuse + specular) * objectColor;
    fragColor = vec4(light, 1.0);
}
"""

startNode = 0
currentNode = 0
endNode = 1

## Drawing function.
#
# Draws primitive.
def display():

    global startNode
    global currentNode
    global endNode

    gl.glClearColor(0.1, 0.1, 0.3, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)

    gl.glUseProgram(program)
    gl.glBindVertexArray(VAO)

    ## Para o vertex shader:
    ## Camera settings:
    view = ut.matTranslate(0.0, 0.0, -5.0)
    loc = gl.glGetUniformLocation(program, "view")
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, view.transpose())
    
    projection = ut.matPerspective(np.radians(45.0), win_width/win_height, 0.1, 100.0)
    loc = gl.glGetUniformLocation(program, "projection")
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, projection.transpose())

    ## Para o fragment shader:
    ## Light settings:
    # Light color.
    loc = gl.glGetUniformLocation(program, "lightColor")
    gl.glUniform3f(loc, 1.0, 1.0, 1.0)
    # Light position.
    loc = gl.glGetUniformLocation(program, "lightPosition")
    gl.glUniform3f(loc, 1.0, 0.0, 2.0)
    # Camera position for the shader.
    loc = gl.glGetUniformLocation(program, "cameraPosition")
    gl.glUniform3f(loc, 0.0, 0.0, -5.0)

    ## Object settings:
    for i in range(0, graphSize):
        # Object pos:
        # transforma cada instância para a posição no grafo
        transformer = ut.matTranslate(graphPos[i][0], graphPos[i][1], graphPos[i][2])
        loc = gl.glGetUniformLocation(program, "model")
        gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, transformer.transpose())

        # Object color:
        # obtém a cor dependendo de qual tipo de nó é. (inicial, atual, final, outro)
        loc = gl.glGetUniformLocation(program, "objectColor")
        if i == startNode:
            gl.glUniform3f(loc, 0.1, 0.5, 0.1)
        elif i == currentNode:
            gl.glUniform3f(loc, 0.1, 0.1, 0.5)
        elif i == endNode:
            gl.glUniform3f(loc, 0.5, 0.1, 0.1)
        else:
            gl.glUniform3f(loc, 0.5, 0.5, 0.1)

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 20*3)

    glut.glutSwapBuffers()


## Reshape function.
# 
# Called when window is resized.
#
# @param width New window width.
# @param height New window height.
def reshape(width,height):

    win_width = width
    win_height = height
    gl.glViewport(0, 0, width, height)
    glut.glutPostRedisplay()


## Keyboard function.
#
# Called to treat pressed keys.
#
# @param key Pressed key.
# @param x Mouse x coordinate when key pressed.
# @param y Mouse y coordinate when key pressed.
def keyboard(key, x, y):

    global type_primitive
    global mode

    if key == b'\x1b'or key == b'q':
        glut.glutLeaveMainLoop()

    glut.glutPostRedisplay()

graphPos = [[]]
graphSize = 1

## Init vertex data.
#
# Defines the coordinates for vertices, creates the arrays for OpenGL.
def initData():

    # Uses vertex arrays.
    global VAO
    global VBO

    global graphPos # Pos dos vértices do grafo
    global graphSize # Quantidade de vértices do grafo

    graphSize = mygraph.GrafoLen
    graphPos = mygraph.Grafo
    graphWeights = mygraph.GrafoWeights

    # ##########################
    icospheres = np.array([
        # coordinate       # normal
        -0.1, -0.1,  0.1,  0.0,  0.0,  1.0,
         0.1, -0.1,  0.1,  0.0,  0.0,  1.0,
         0.1,  0.1,  0.1,  0.0,  0.0,  1.0,
        -0.1, -0.1,  0.1,  0.0,  0.0,  1.0,
         0.1,  0.1,  0.1,  0.0,  0.0,  1.0,
        -0.1,  0.1,  0.1,  0.0,  0.0,  1.0,
         0.1, -0.1,  0.1,  1.0,  0.0,  0.0, 
         0.1, -0.1, -0.1,  1.0,  0.0,  0.0,
         0.1,  0.1, -0.1,  1.0,  0.0,  0.0,
         0.1, -0.1,  0.1,  1.0,  0.0,  0.0,
         0.1,  0.1, -0.1,  1.0,  0.0,  0.0,
         0.1,  0.1,  0.1,  1.0,  0.0,  0.0,
         0.1, -0.1, -0.1,  0.0,  0.0, -1.0,
        -0.1, -0.1, -0.1,  0.0,  0.0, -1.0,
        -0.1,  0.1, -0.1,  0.0,  0.0, -1.0,
         0.1, -0.1, -0.1,  0.0,  0.0, -1.0,
        -0.1,  0.1, -0.1,  0.0,  0.0, -1.0,
         0.1,  0.1, -0.1,  0.0,  0.0, -1.0,
        -0.1, -0.1, -0.1, -1.0,  0.0,  0.0,
        -0.1, -0.1,  0.1, -1.0,  0.0,  0.0,
        -0.1,  0.1,  0.1, -1.0,  0.0,  0.0,
        -0.1, -0.1, -0.1, -1.0,  0.0,  0.0,
        -0.1,  0.1,  0.1, -1.0,  0.0,  0.0,
        -0.1,  0.1, -0.1, -1.0,  0.0,  0.0,
        -0.1,  0.1,  0.1,  0.0,  1.0,  0.0,
         0.1,  0.1,  0.1,  0.0,  1.0,  0.0,
         0.1,  0.1, -0.1,  0.0,  1.0,  0.0,
        -0.1,  0.1,  0.1,  0.0,  1.0,  0.0,
         0.1,  0.1, -0.1,  0.0,  1.0,  0.0,
        -0.1,  0.1, -0.1,  0.0,  1.0,  0.0,
        -0.1, -0.1,  0.1,  0.0, -1.0,  0.0,
        -0.1, -0.1, -0.1,  0.0, -1.0,  0.0,
         0.1, -0.1,  0.1,  0.0, -1.0,  0.0,
        -0.1, -0.1, -0.1,  0.0, -1.0,  0.0,
         0.1, -0.1, -0.1,  0.0, -1.0,  0.0,
         0.1, -0.1,  0.1,  0.0, -1.0,  0.0
    ], dtype='float32')

    VAO = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(VAO)

    VBO = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, VBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, icospheres.nbytes, icospheres, gl.GL_STATIC_DRAW)
    
    # Set attributes.
    # Pos
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*icospheres.itemsize, None)
    gl.glEnableVertexAttribArray(0)
    # Normal
    gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*icospheres.itemsize, c_void_p(3*icospheres.itemsize))
    gl.glEnableVertexAttribArray(1)

    ##########################

    # Unbind Vertex Array Object.
    gl.glBindVertexArray(0)

    gl.glEnable(gl.GL_DEPTH_TEST)


## Create program (shaders).
#
# Compile shaders and create programs.
def initShaders():

    global program

    program = ut.createShaderProgram(vertex_code, fragment_code)


## Main function.
#
# Init GLUT and the window settings. Also, defines the callback functions used in the program.
def main():

    glut.glutInit()
    glut.glutInitContextVersion(3, 3);
    glut.glutInitContextProfile(glut.GLUT_CORE_PROFILE);
    glut.glutInitDisplayMode(glut.GLUT_DOUBLE | glut.GLUT_RGBA | glut.GLUT_DEPTH)
    glut.glutInitWindowSize(win_width,win_height)
    glut.glutCreateWindow('Dijkstra 3D')

    # Init vertex data for the triangle.
    initData()
    
    # Create shaders.
    initShaders()

    glut.glutReshapeFunc(reshape)
    glut.glutDisplayFunc(display)
    glut.glutKeyboardFunc(keyboard)

    glut.glutMainLoop()

if __name__ == '__main__':
    main()
