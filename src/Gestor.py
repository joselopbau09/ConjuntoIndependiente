
import copy
from Graph import Graph
import random 

class Gestor:
    
    def __init__(self,graph):
        self.grafica = graph
        self.conjuntoIndependiente = []
        self.verticesQuitados = []
        self.graficas = []

    def setGrafica(self, grafica):
        self.grafica = grafica

    def trianguloGraph(self, graph):
        for vertices in graph:
            if len(vertices.adjacent) != 1:
                return False
        vertices = list(graph.getVertices())    
        v1 = graph.vertDictionery[vertices[0]]
        v2 = graph.vertDictionery[vertices[1]]
        v3 = graph.vertDictionery[vertices[2]]
        if v1 in v2.adjacent:
            if v3 in v1.adjacent:
                if v2 in v3.adjacent:
                    return True
        else:
            if v2 in v1.adjacent:
                if v3 in v2.adjacent:
                    return True

    def verticesNoCiclicos(self,graph):
        candidatos = []
        verticesInd = []

        for v in graph:
            for n in graph:
                if v != n:
                    if (v not in n.adjacent):
                        candidatos.append(True)
                    else:
                        candidatos.append(False)
            if False not in candidatos:
                verticesInd.append(v)
            candidatos.clear()
        return verticesInd    
    
    def casoBaseConjuntoIndependiente(self):
        noHayAdjacentes = []
        vertices = self.grafica.getVertices()
        
        if (len(vertices) == 3 and self.trianguloGraph(self.grafica)):
            vertices = list(self.grafica.getVertices())
            self.grafica.vertDictionery[vertices[0]].addConjuntoIdependiente() 
            self.conjuntoIndependiente.append(self.grafica.vertDictionery[vertices[0]])
            return 
        for vertices in self.grafica:
            if len(vertices.adjacent) == 0:
                noHayAdjacentes.append(True)
            else:
                noHayAdjacentes.append(False)    
        if False not in  noHayAdjacentes:
            for vertice in self.grafica:
                self.conjuntoIndependiente.append(vertice)
                vertices.addConjuntoIdependiente()

            return
        else:
            verticesInd = self.verticesNoCiclicos(self.grafica)
            for vertice in verticesInd:
                self.conjuntoIndependiente.append(vertice)
                vertice.addConjuntoIdependiente()                
            return    
    
    def removerVecindad(self, vertice):
        listaVecinos = []
        vecinos = []
        graficaCopia = copy.deepcopy(self.grafica) 
        self.graficas.append(graficaCopia)

        verticeRemovido = self.grafica.vertDictionery.pop(vertice)
        listaVecinos = list(verticeRemovido.adjacent.keys())
        
        if len(listaVecinos) != 0:
            i = 0
            while len(listaVecinos) > i:
                vecinos.append(self.grafica.vertDictionery.pop(listaVecinos[i].id))
                i += 1

            j = 0
            while len(vecinos) > j:
                for vertice in self.grafica:
                    if vecinos[j] in vertice.adjacent:
                        vertice.adjacent.pop(vecinos[j])
                j += 1       
        x = list(self.grafica.vertDictionery.keys())
        for v in x:
            if verticeRemovido in self.grafica.vertDictionery[v].adjacent:
                self.grafica.vertDictionery[v].adjacent.pop(verticeRemovido)

    def seleccionaVertice(self):
        vertices = list(self.grafica.vertDictionery.keys())
        if len(vertices) == 0:
            return -1
        return random.choice(vertices)

    def obtencionConjuntoIndependiente(self, graph):
        self.setGrafica(graph) 
        nueva = self.grafica
        tamano = list(self.grafica.vertDictionery.keys())
        if len(tamano) < 4:
            self.casoBaseConjuntoIndependiente()
            return

        vertice = self.seleccionaVertice()
        self.verticesQuitados.append(vertice)

        self.removerVecindad(vertice)
        
        self.obtencionConjuntoIndependiente(nueva)

    def verificaIndependencia(self):
        conjuntoInd = self.conjuntoIndependiente
        while len(self.verticesQuitados) != 0:
            verticeId = self.verticesQuitados.pop()
            grafica = self.graficas.pop()
            vertice = grafica.getVertex(verticeId)
            noAdyacentes = True
            
            for v in conjuntoInd:
                if vertice in v.adjacent.keys():
                    noAdyacentes = False
                    break

            if noAdyacentes:
                conjuntoInd.append(vertice)
        return conjuntoInd                
    
    def refinacionConjunto(self,conjuntoInd, grafica):
        conjunto = conjuntoInd
        for vertices in conjunto:
            for v in grafica:
                ady = list(v.adjacent.keys())
                lista = []
                for x in ady:
                    lista.append(x.getverticeId())
                if vertices.getverticeId() in lista:
                    if vertices in conjunto:
                        conjunto.remove(vertices)
        return conjunto


    def imprimeConjuntoInd(self, grafica):
        conjunto = self.verificaIndependencia()
        conjuntoInd = self.refinacionConjunto(conjunto,grafica)
        i = 0
        cadena = '['
        while len(conjuntoInd) > i:
            cadena += f'{conjuntoInd[i].id}, '
            i += 1
        cadena += ']'    
        print(cadena)