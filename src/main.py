
import copy
from Independiente import Independiente
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

    grafica1 = lecturaArchivo('graph1.txt')
    grafica2 = lecturaArchivo('graph2.txt')
    grafica3 = lecturaArchivo('graph3.txt')

    graficaCop1 = copy.deepcopy(grafica1)
    graficaCop2 = copy.deepcopy(grafica2)
    graficaCop3 = copy.deepcopy(grafica3)

    indUno = Independiente(grafica1)
    indDos = Independiente(grafica2)
    indTres = Independiente(grafica3)

    print('Ejemplos 1:')
    indUno.obtencionConjuntoIndependiente(grafica1)
    indUno.imprimeConjuntoInd(graficaCop1)
    
    print('Ejemplos 2:')
    indDos.obtencionConjuntoIndependiente(grafica2)
    indDos.imprimeConjuntoInd(graficaCop2)

    print('Ejemplos 3:')
    indTres.obtencionConjuntoIndependiente(grafica3)
    indTres.imprimeConjuntoInd(graficaCop3)

main()    