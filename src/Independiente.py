
from Graph import Graph

class Independiente:
    
    def __init__(self):
        self.grafica = Graph()
        self.conjuntoIndependiente = []

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
    
    def getVerticesIndependientes(self, graph):
        noHayAdjacentes = []
        self.grafica = graph
        vertices = self.grafica.getVertices()
        
        if (len(vertices) == 3 and self.trianguloGraph(self.grafica)):
            vertices = list(graph.getVertices())
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
    
    def imprimeConjuntoInd(self):
        print(self.conjuntoIndependiente)

                
if __name__== '__main__':
    G  = Graph()
    G.addVertex('a')        
    #G.addVertex('b')        
    #G.addVertex('c')        
    #G.addVertex('d')        
    #G.addVertex('e')
    #G.addEdge('b', 'a')
    #G.addEdge('b','c')
    #G.addEdge('c','a')
    #G.addEdge('c', 'b')
    #G.addEdge('d', 'e')
    
    x = Independiente()
    x.getVerticesIndependientes(G)
    x.imprimeConjuntoInd()                
