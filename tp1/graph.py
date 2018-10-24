from node import Node
from edge import Edge


class Graph:

    def __init__(self, fileName):
        self.fileName = fileName
        self.nodes = []
        self.edges = []
        self.linkedNodes = {}

    def createNode(self, numero, recharge):
        node = Node(numero, recharge)
        self.nodes.append(node)
    
    def createEdge(self, node1, node2, time):
        edge = Edge(self.nodes[node1], self.nodes[node2], time)
        self.edges.append(edge)

    def readFile(self):
        with open(self.fileName) as file:
            for line in file:
                if 2 < len(line):
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
        for i in self.linkedNodes:
            str = '('
            str += i + ', ' + self.node(i).getRecharge() + ', ('
            for j in self.linkedNodes[i]:
                str += ('(' + j + ', ' + self.getTime(i, j)) + '), '
            str = str[:-2] + '))'
            print(str)


    def createGraph(self):
        self.readFile()
        for edge in self.edges:
            if edge.getDeparture().getNumber() in self.linkedNodes:
                self.linkedNodes[edge.getDeparture().getNumber()].append(edge.getDestination().getNumber())
            else:
                self.linkedNodes[edge.getDeparture().getNumber()] = [edge.getDestination().getNumber()]


    def getTime(self, node1, node2):
        for edge in self.edges:
            if (edge.getDeparture().getNumber() == node1 and edge.getDestination().getNumber() == node2) or (edge.getDeparture().getNumber() == node2 and edge.getDestination().getNumber() == node1):
                return str(edge.getTime())

    def node(self, num):
        return self.nodes[int(num)-1]