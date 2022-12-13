from math import sqrt


mode = "graph"

def mutateObject():
    origem = open("plane.obj")
    if mode == "graph":
        destino = open("graph.py", "w")
    else:
        destino = open("objects.py", "w")
    
    destino.write("import numpy as np\n\n")

    vertices = []
    verticesQt = 0
    normals = []

    origem.readline()
    origem.readline()
    origem.read(2)
    objName = origem.readline().strip()

    # Get vertices
    buffer = origem.read(2)
    while buffer == "v ":
        verticesQt += 1
        invalues = origem.readline().strip().split(" ")
        for value in invalues:
            vertices.append(float(value))
        buffer = origem.read(2)
        
    
    # Get vertex normals
    if buffer == "vn":
        while buffer == "vn":
            invalues = origem.readline().split()
            for value in invalues:
                normals.append(float(value))
            buffer = origem.read(2)
        origem.readline() # s off
    
    facebuffer = []

    # Get faces
    if mode == "object":
        destino.write(objName + " = np.array([\n")

        buffer = origem.read(2)
        while buffer == "f ": # for each face
            facebuffer = origem.readline().strip().split(' ')
            #3 points *
            #3cd vertex + 3cd normals
            for j in range(0, 3):
                for i in range(0, 3):
                    iindex = int(facebuffer[j].split("//")[0])
                    destino.write(str(vertices[(iindex-1)*3+i]))
                    destino.write(", ")
                for i in range(0, 3):
                    iindex = int(facebuffer[j].split("//")[1])
                    destino.write(str(normals[(iindex-1)*3+i]))
                    destino.write(", ")
                destino.write("\n")
            destino.write("\n")
            buffer = origem.read(2)
            destino.write("], dtype='float32')")

    elif mode == "graph":
        # Vertices
        destino.write(objName + "Pos = [\n")
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

        destino.write("\n" + objName + "Len = " + str(verticesQt) + "\n")

        # Edges
        destino.write("\n" + objName + "Mesh = np.array([\n")
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

        # Adjecency Matrix
        destino.write("\n" + objName + "Weights = [\n")
        adjacency = []
        # Calcula a matriz de adjacência
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
    mutateObject()