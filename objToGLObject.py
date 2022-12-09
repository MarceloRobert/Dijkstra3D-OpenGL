def mutateObject():
    origem = open("icosphere.obj")
    destino = open("objects.py", "w")
    vertices = []
    normals = []

    origem.readline()
    origem.readline()
    origem.read(2)
    destino.write("import numpy as np\n\n")
    destino.write(origem.readline().strip() + " = np.array([\n")

    # Get vertices
    buffer = origem.read(2)
    while buffer == "v ":
        invalues = origem.readline().strip().split(" ")
        for value in invalues:
            vertices.append(float(value))
        buffer = origem.read(2)
        
    
    # Get vertex normals
    while buffer == "vn":
        invalues = origem.readline().split()
        for value in invalues:
            normals.append(float(value))
        buffer = origem.read(2)
    
    origem.readline() # s off
    
    facebuffer = []

    # Get faces
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

    origem.close()
    destino.close()
    return

if __name__ == "__main__":
    mutateObject()