from dis import dis
import imp


import sys

class Vertice:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        # Set distance to infinity for all nodes
        self.distance = sys.maxsize
        # Marked all nodes unvisited 
        self.visted = False
        # Predecessor
        self.previous = None

    def addNeighbor(self, neighbor, weight = 0):    
        self.adjacent[neighbor] = weight

    def getConnection(self):
        return self.adjacent.keys()

    def getverticeId(self):
        return self.id

    def setDistance(self, dist):
        self.distance = dist

    def getDistance(self):
        return self.distance 

    def setPrevious(self, prev):
        self.previous = prev

    def setVisited(self):
        self.visted = True

    def __str__(self):
        return f'{str(self.id)} adjacent: {str([x.id for x in self.adjacent])}'                    

class Graph:
    def __init__(self):
        self.vertDictionery = {}
        self.numVertices = 0

    def __iter__(self):
        return iter(self.vertDictionery.values())

    def addVertex(self ,node):
        self.numVertices += 1
        newVertex = Vertice(node)
        self.vertDictionery[node] = newVertex
        return newVertex

    def getVertex(self, n):     
        if n  in self.vertDictionery:
            return self.vertDictionery[n]
        else:
            return None

    def addEdge(self, frm, to, cost = 0):
        if frm not in self.vertDictionery:
            self.addVertex(frm)
        if to not in self.vertDictionery:
            self.addVertex(to)
        self.vertDictionery[frm].addNeighbor(self.vertDictionery[to], cost)

    def getVertices(self):
        return self.vertDictionery.keys()

    def setPrevious(self,current):                                
        self.previous = current

    def getPrevious(self):                                
        return self.previous 

    def getEdges(self):
        edges = []
        for v in G:
            for w in v.getConnection():
                vid = v.getverticeId()    
                wid = w.getverticeId()
                edges.append((vid, wid))
        return edges

if __name__== '__main__':
    G  = Graph()
    G.addVertex('a')        
    G.addVertex('b')        
    G.addVertex('c')        
    G.addVertex('d')        
    G.addVertex('e')
    G.addEdge('a', 'b')
    G.addEdge('a','c')
    G.addEdge('b','e')
    G.addEdge('c', 'd')
    G.addEdge('d', 'e')

    print('Graph datos:')
    print(G.getEdges())
    