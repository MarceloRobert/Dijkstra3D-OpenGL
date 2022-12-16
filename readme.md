# Execução do algoritmo Dijkistra no espaço 3D com representação gráfica

## Autores:
## Flávio Augusto Aló Torres <br> Gabriel Rocha Gandur <br> Luan Rodrigues Munholi <br> Lucas Batista Pereira <br> Marcelo Robert Santos

### Execução do programa:

São necessários os pacotes:

-  libpython3-dev;
- python3-pip;
- numpy; e
- pyopengl.

Os pacotes libpython3-dev e python3-pip podem ser instalados pelo synaptic, como nos pacotes anteriores.

Para instalar o numpy e o pyopengl, você deve executar os comandos (certifique-se que o PIP esteja atualizado):

- $ pip3 install numpy

- $ pip3 install pyopengl

OBS: Caso o PIP esteja desatualizado, use o seguinte comando para atualizar: 

- $ python -m pip install --upgrade pip

É necessário que as bibliotecas e arquivos locais estejam presentes no mesmo diretório do programa principal, estes arquivos são:

- graph.py
- objects.py
- utils.py

Para a transformação de um objeto para o grafo do programa, é necessário o arquivo "objToGLObject.py", e a pasta "objetos" com os objetos dentro.

Assim que todos os pacotes estiverem instalados, basta executar o seguinte comando no local do programa.

- $ python3 dijkstra.py

Irá abir uma tela projetando um grafo em 3D, o grafo em questão existe num outro documento no mesmo local do programa executável. O usuário poderá executar os seguintes comando para interagir com o grafo: 


-   "W" ou "w": rotação positivo em x <br>
    "S" ou "s": rotação negativo em x <br>
    "D" ou "d": rotação positivo em y <br>
    "A" ou "a": rotação negativo em y <br>
    "E" ou "e": rotação positivo em z <br>
    "Q" ou "q": rotação negativo em z

-   "I" ou "i": aumentar escala <br>
    "O" ou "o": diminuir escala

-   "M" ou "m": aumentar zoom <br>
    "N" ou "n": diminuir zoom

-   "H" ou "h": Iniciar o Dijkstra <br>
    "P" ou "p": Iterar sobre o menor caminho entre origem o destino (Essa função apenas funciona após ativar o Algoritimo de Dijkstra).

Ao pressionar a tecla "h" ou "H", será solicitada uma entrada no terminal onde o programa foi executado, onde o usuário deve passar o nó inicial e final para a execução do algoritmo de Dijkistra.

### Para a modificação do grafo:

Caso queira, é possível modificar o grafo que é apresentado, para isso, entre no arquivo "objToGLObject.py" e mude o nome do arquivo de entrada na função main para o nome do arquivo desejado.

É possível adicionar objetos customizados; esses objetos não devem conter faces e devem ser exportados apenas com os vértices e arestas.