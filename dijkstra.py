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

instanceVAO = None
instanceVBO = None
graphVAO = None
graphVBO = None
graphEBO = None

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
endNode = 0
caminhoNode = []
pathAtoB = []
flagDijkstra = False

def dijkstra(graph, start):
    
    # Inicialização dos vectors
    distances = [float("inf") for _ in range(len(graph))]
    visited = [False for _ in range(len(graph))]
    distances[start] = 0

    # Esse vector guarda o caminho
    global parents 
    parents = [float(-1) for _ in range(len(graph))]

    # Dijkstra
    while True:

        shortest_distance = float("inf")
        shortest_index = -1
        for i in range(len(graph)):
            if distances[i] < shortest_distance and not visited[i]:
                shortest_distance = distances[i]
                shortest_index = i

        if shortest_index == -1:
            return distances

        for i in range(len(graph[shortest_index])):
            if graph[shortest_index][i] != 0 and distances[i] > distances[shortest_index] + graph[shortest_index][i]:
                parents[i] = shortest_index
                distances[i] = distances[shortest_index] + graph[shortest_index][i]

        visited[shortest_index] = True

# Print do caminho
def printPath(j):
    global pathAtoB

    pathAtoB.clear()
    pathAtoB.append(startNode)

    if parents[j] == -1:
        return
    
    printPath(parents[j])

    pathAtoB.append(j)

## Drawing function.
#
# Draws primitive.
def display():
    global startNode
    global currentNode
    global endNode
    global caminhoNode
    global rotate_inc_x
    global rotate_inc_y
    global rotate_inc_z
    global scale_inc
    global zoom
    global flagDijkstra
    global pathAtoB

    gl.glClearColor(0, 0, 0, 1.0)
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glUseProgram(program)


    # Desenha as "instâncias"
    gl.glBindVertexArray(instanceVAO)
    ## Para o vertex shader:
    ## Camera settings:

    
    Rx = ut.matRotateX(np.radians(0.0+rotate_inc_x))
    Ry = ut.matRotateY(np.radians(0.0+rotate_inc_y))
    Rz = ut.matRotateZ(np.radians(0.0+rotate_inc_z))
    Mz = ut.matTranslate(0.0, 0.0, -10.0)

    view = np.matmul(Mz, Rx)
    view = np.matmul(view, Ry)
    view = np.matmul(view, Rz)
    loc = gl.glGetUniformLocation(program, "view")
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, view.transpose())
    
    projection = ut.matPerspective(np.radians(zoom), win_width/win_height, 0.1, 100.0)
    loc = gl.glGetUniformLocation(program, "projection")
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, projection.transpose())

    ## Para o fragment shader:
    ## Light settings:
    # Light color.
    loc = gl.glGetUniformLocation(program, "lightColor")
    gl.glUniform3f(loc, 1.0, 1.0, 1.0)
    # Light position.
    loc = gl.glGetUniformLocation(program, "lightPosition")
    gl.glUniform3f(loc, 5.0, 5.0, 30.0)
    # Camera position for the shader.
    loc = gl.glGetUniformLocation(program, "cameraPosition")
    gl.glUniform3f(loc, 0.0, 0.0, -5.0)

    ## Object settings:
    for i in range(0, graphSize):
        # Object pos:
        # transforma cada instância para a posição no grafo
        transformer = ut.matTranslate(graphPos[i][0], graphPos[i][1], graphPos[i][2])
        Sg = ut.matScale(scale_inc, scale_inc, scale_inc)
        transformer = np.matmul(transformer, Sg)
        loc = gl.glGetUniformLocation(program, "model")
        gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, transformer.transpose())

        # Object color:
        # obtém a cor dependendo de qual tipo de nó é. (inicial, atual, final, outro)
        loc = gl.glGetUniformLocation(program, "objectColor")

        if flagDijkstra:
            if i == startNode:
                gl.glUniform3f(loc, 0.1, 0.5, 0.1)
            elif i == endNode:
                gl.glUniform3f(loc, 0.5, 0.1, 0.1)
            elif i == pathAtoB[currentNode]:
                gl.glUniform3f(loc, 0.1, 0.1, 0.5)
            elif i in caminhoNode:
                gl.glUniform3f(loc, 0.5, 0.1, 0.5)
            else:
                gl.glUniform3f(loc, 0.5, 0.5, 0.1)
        else:
            gl.glUniform3f(loc, 0.5, 0.5, 0.1)

        gl.glDrawArrays(gl.GL_TRIANGLES, 0, 20*3)
    gl.glUniform3f(loc, 1, 1, 1) # reseta a cor para amarelo
    

    # Desenha o grafo
    gl.glBindVertexArray(graphVAO)
    gl.glPointSize(5)
    # Reseta o posicionamento para desenhar o grafo
    model=np.identity(4)
    loc = gl.glGetUniformLocation(program, "model")
    gl.glUniformMatrix4fv(loc, 1, gl.GL_FALSE, model.transpose())

    gl.glLineWidth(5)
    gl.glDrawArrays(gl.GL_LINES, 0, mygraph.GrafoMeshLen)

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
    # viewport centralizado, aspecto 1:1
    if(height > width):
        gl.glViewport(0, int((height-width)/2), width, width)
    else:
        gl.glViewport(int((width-height)/2), 0, height, height)
    glut.glutPostRedisplay()

rotate_inc_x = 0.0
rotate_inc_y = 0.0
rotate_inc_z = 0.0
scale_inc = 1.0
zoom = 45.0

## Keyboard function.
#
# Called to treat pressed keys.
#
# @param key Pressed key.
# @param x Mouse x coordinate when key pressed.
# @param y Mouse y coordinate when key pressed.
def keyboard(key, x, y):

    global startNode
    global endNode
    global caminhoNode
    global currentNode

    global rotate_inc_x
    global rotate_inc_y
    global rotate_inc_z
    global scale_inc
    global zoom

    global flagDijkstra
    global graphSize

    if key == b'\x1b':
        glut.glutLeaveMainLoop()
        
    if key == b'a':
        rotate_inc_y -= 2

    if key == b'd':
        rotate_inc_y += 2

    if key == b'w':
        rotate_inc_x += 2

    if key == b's':
        rotate_inc_x -= 2

    if key == b'e':
        rotate_inc_z += 2

    if key == b'q':
        rotate_inc_z -= 2
    
    if key == b'i':
        scale_inc += 0.25
    
    if key == b'o':
        if scale_inc > 0:
            scale_inc -= 0.25
    
    if key == b'm':
        zoom += 2
    
    if key == b'n':
        if zoom >= 0:
            zoom -= 2

    if key == b'h':
        currentNode = 0
        caminhoNode.clear()
        startNode = int(input('Nó de origem: '))
        if startNode < 0 or startNode >= graphSize:
            print("Índice fora dos limites do grafo")
            print("Maior índice possível: ", graphSize-1)
        else:
            dijkstra(mygraph.GrafoWeights, startNode)

            endNode = int(input('Nó de destino: '))
            if endNode < 0 or endNode >= graphSize:
                print("Índice fora dos limites do grafo")
                print("Maior índice possível: ", graphSize-1)
            else:
                printPath(endNode)

                print("Caminho da origem até destinho:")
                print(pathAtoB)

                flagDijkstra = True
                display()
    
    if key == b'p':
        if flagDijkstra:
            if currentNode < len(pathAtoB)-1:
                caminhoNode.append(pathAtoB[currentNode])
                currentNode += 1


    glut.glutPostRedisplay()

graphPos = [[]]
graphSize = 1

#def animacao(origem, destino)


## Init vertex data.
#
# Defines the coordinates for vertices, creates the arrays for OpenGL.
def initData():

    # Uses vertex arrays.
    global instanceVAO
    global instanceVBO
    global graphVAO
    global graphVBO
    global graphEBO

    global graphPos # Pos dos vértices do grafo
    global graphSize # Quantidade de vértices do grafo

    graphSize = mygraph.GrafoLen
    graphPos = mygraph.GrafoPos
    graphMesh = mygraph.GrafoMesh

    graphVAO = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(graphVAO)

    graphVBO = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, graphVBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, graphMesh.nbytes, graphMesh, gl.GL_STATIC_DRAW)
    
    # Set attributes.
    # Pos
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 3*graphMesh.itemsize, None)
    gl.glEnableVertexAttribArray(0)

    # ##########################
    icospheres = myobj.Cube

    instanceVAO = gl.glGenVertexArrays(1)
    gl.glBindVertexArray(instanceVAO)

    instanceVBO = gl.glGenBuffers(1)
    gl.glBindBuffer(gl.GL_ARRAY_BUFFER, instanceVBO)
    gl.glBufferData(gl.GL_ARRAY_BUFFER, icospheres.nbytes, icospheres, gl.GL_STATIC_DRAW)
    
    # Set attributes.
    # Pos
    gl.glVertexAttribPointer(0, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*icospheres.itemsize, None)
    gl.glEnableVertexAttribArray(0)
    # Normal
    gl.glVertexAttribPointer(1, 3, gl.GL_FLOAT, gl.GL_FALSE, 6*icospheres.itemsize, c_void_p(3*icospheres.itemsize))
    gl.glEnableVertexAttribArray(1)

    # #########################

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
    glut.glutInitContextVersion(3, 3)
    glut.glutInitContextProfile(glut.GLUT_CORE_PROFILE)
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
