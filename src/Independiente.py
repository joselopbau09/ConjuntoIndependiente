
from copy import copy
from Graph import Graph

class Independiente:
    
    def __init__(self, graph):
        self.grafica = graph
        self.conjuntoIndependiente = []
        self.graficas = []

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
    
    def getVerticesIndependientes(self):
        noHayAdjacentes = []
        vertices = self.grafica.getVertices()
        
        if (len(vertices) == 3 and self.trianguloGraph(self.grafica)):
            vertices = list(self.graph.getVertices())
            self.grafica.vertDictionery[vertices[0]].addConjuntoIdependiente() 
            self.conjuntoIndependiente.append(self.grafica.vertDictionery[vertices[0]].id)
            return 
        for vertices in self.grafica:
            if len(vertices.adjacent) == 0:
                noHayAdjacentes.append(True)
            else:
                noHayAdjacentes.append(False)    
        if False not in  noHayAdjacentes:
            for vertice in self.grafica:
                self.conjuntoIndependiente.append(vertice.id)
                vertices.addConjuntoIdependiente()

            return
        else:
            verticesInd = self.verticesNoCiclicos(self.grafica)
            for vertice in verticesInd:
                self.conjuntoIndependiente.append(vertice.id)
                vertice.addConjuntoIdependiente()                
            return    
    
    def removerVecindad(self, vertice):
        listaVecinos = []
        vecinos = []
        graficaCopia = copy(self.grafica) 
        self.graficas.append(graficaCopia)

        verticeRemovido = self.grafica.vertDictionery.pop(vertice)

        listaVecinos = list(verticeRemovido.adjacent.keys())
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

    def imprimeConjuntoInd(self):
        print(self.conjuntoIndependiente)
                
if __name__== '__main__':
    G  = Graph()
    G.addVertex('a')        
    G.addVertex('b')        
    G.addVertex('c')        
    G.addVertex('d')        
    G.addVertex('e')
    G.addVertex('f')
    G.addEdge('b', 'a')
    G.addEdge('b','c')
    G.addEdge('d','c')
    G.addEdge('d', 'e')
    G.addEdge('e', 'f')
    
    x = Independiente(G)

    x.removerVecindad('d')

    """ 
    verticeRemovido = G.vertDictionery.pop('d')
    print(verticeRemovido.adjacent)
    listavecinos = list(verticeRemovido.adjacent.keys())
    vecinos1 = G.vertDictionery.pop(listavecinos[0].id)
    vecinos2 = G.vertDictionery.pop(listavecinos[1].id)
    print(verticeRemovido.adjacent[vecinos1]) """

    for x in G:
        print(x.id)
