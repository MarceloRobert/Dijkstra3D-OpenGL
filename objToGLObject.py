from math import sqrt

def mutateObject(filename):
    origem = open(filename)
    destino = open("graph.py", "w")
    
    destino.write("import numpy as np\n\n")

    vertices = []
    verticesQt = 0

    # Remove Blender Headers
    origem.readline()
    origem.readline()

    buffer = origem.read(2)
    if buffer == "o ":
        origem.readline() # tira o nome do objeto
        buffer = origem.read(2)

    # Get vertices
    while buffer == "v ":
        verticesQt += 1
        invalues = origem.readline().strip().split(" ")
        for value in invalues:
            vertices.append(float(value))
        buffer = origem.read(2)

    # Vertices
    destino.write("GrafoPos = [\n")
    # Saves vertices into file
    for i in range(0, verticesQt):
        destino.write("\t[")
        for j in range(0, 3):
            destino.write(str(vertices[i*3+j]))
            if j != 2:
                destino.write(", ")
            else:
                destino.write("],\n")
    destino.write("]\n")

    destino.write("\nGrafoLen = " + str(verticesQt) + "\n")

    # Edges
    destino.write("\nGrafoMesh = np.array([\n")
    edges = []
    edgesQt = 0
    # Get edges
    while buffer == "l ":
        edgesQt += 1
        invalues = origem.readline().strip().split(" ")
        edges.append([int(invalues[0])-1, int(invalues[1])-1])
        buffer = origem.read(2)
        # Saves edge into file
        destino.write("\t")
        iindex = int(invalues[0])
        for i in range(0, 3):
            destino.write(str(vertices[(iindex-1)*3+i]) + ", ")
        destino.write("\n\t")
        iindex = int(invalues[1])
        for i in range(0, 3):
            destino.write(str(vertices[(iindex-1)*3+i]) + ", ")
        destino.write("\n")
    destino.write("], dtype='float32')\n")

    # Save edge length into file
    destino.write("\nGrafoMeshLen = " + str(len(edges)*2) + "\n")

    # Adjacency Matrix
    destino.write("\nGrafoWeights = [\n")
    adjacency = []
    # Calculates it
    for i in range(0, verticesQt):
        adjacency.append([])
        for j in range(0, verticesQt):
            adjacency[i].append(0)
    for i in range(0, edgesQt):
        varweight = weight(vertices, edges[i][0], edges[i][1])
        adjacency[edges[i][0]][edges[i][1]] = varweight
        adjacency[edges[i][1]][edges[i][0]] = varweight
    # Saves AdjMatrix into file
    for i in range(0, verticesQt):
        destino.write("\t[")
        for j in range(0, verticesQt):
            destino.write(str(adjacency[i][j]))
            if j != verticesQt-1:
                destino.write(", ")
            else:
                destino.write("],\n")
    destino.write("]\n")

    origem.close()
    destino.close()
    return

def weight(vertices, vertexid1, vertexid2):
    dz = vertices[vertexid1*3+2] - vertices[vertexid2*3+2]
    dy = vertices[vertexid1*3+1] - vertices[vertexid2*3+1]
    dx = vertices[vertexid1*3] - vertices[vertexid2*3]

    return sqrt(dz*dz + dy*dy + dx*dx)

if __name__ == "__main__":
    mutateObject("plane.obj")