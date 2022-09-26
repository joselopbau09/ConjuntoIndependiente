
from Graph import Graph

def lecturaArchivo(nombre):
    listaLineas = []
    with open(nombre) as archivo:
        listaLineas = archivo.readlines()
    grafica = creacionGrafica(listaLineas.pop(0))
    return unirVertices(listaLineas, grafica)

def creacionGrafica(cadena):
    grafica = Graph()
    listaVertices  = cadena.split(',')
    eliminarSalto = listaVertices[len(listaVertices) - 1].replace('\n','')
    listaVertices[len(listaVertices) - 1] = eliminarSalto
    for vertice in listaVertices:
        grafica.addVertex(vertice)
            
    return grafica

def unirVertices(listaCadenas, grafica):
    graph = grafica
    for cadena in listaCadenas:
        listaAristas  = cadena.split(',')
        eliminarSalto = listaAristas[1].replace('\n','')
        listaAristas[1] = eliminarSalto
        graph.addEdge(listaAristas[0], listaAristas[1])
    return graph    

def main():

    lecturaArchivo('graph.txt')

main()    