from node import Node
from edge import Edge


class Graph:

    def __init__(self, fileName):
        self.fileName = fileName
        self.nodes = []
        self.edges = []
        self.linkedNodes = {}

    def createNode(self, numero, recharge):
        node = node(numero, recharge)
        self.nodes.append(node)
    
    def createEdge(self, node1, node2, time):
        edge = edge(self.nodes[node1], self.nodes[node2], time)
        self.edges.append(edge)

    def readFile(self):
        with open(self.fileName) as file:
            for line in file:
                if line != '\n':
                    words = [word.strip() for word in line.split(',')]
                    self.createNode(words[0], words[1])
                else:
                    break
            for line in file:
                    words = [word.strip() for word in line.split(',')]
                    node1 = int(words[0]) - 1
                    node2 = int(words[1]) - 1
                    time = int(words[2])
                    self.createEdge(node1, node2, time)
        file.close()
    
    def printGraph(self):
        print(self.linkedNodes)

    def createGraph(self):
        self.readFile()
        for edge in self.edges:
            if linkedNodes[edge.getDeparture] is None:
                linkedNodes[edge.getDeparture] = [edge.getDestination]
            else:
                linkedNodes[edge.getDeparture].append(edge.getDestination)

    def getTime(self, node1, node2):
        for edge in self.edges:
            if (edge.departure == node1 & edge.destination == node2) | (edge.departure == node2 & edge.destination == node1):
                return edge.time