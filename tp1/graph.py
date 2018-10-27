from node import Node
from edge import Edge
from collections import deque
import copy

inf = float('inf')    

class Graph:

    def __init__(self, fileName):
        self.fileName = fileName
        self.nodes = []
        self.edges = []
        self.linkedNodes = {}

    # def __init__(self, fileName, nodes, edges):
    #     self.fileName = fileName
    #     self.nodes = nodes
    #     self.edges = edges
    #     self.linkedNodes = {}

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
        for departure in self.linkedNodes:
            print(departure)
            string = '('
            string += departure.numero + ', ' + departure.recharge + ', ('

            for destination in self.linkedNodes[departure]:
                string += ('(' + destination + ', ' + destination.time + '), '

            # string = string[:-2] + '))'

            print(string)

    # {
    #     1: [Edge(1,2,99), Edge(1,3, 60)],
    #     2: [Edge(2,4,9), Edge(2,1, 99)]
    # }

    def createGraph(self):
        self.readFile()
        for edge in self.edges:
            if edge.departure in self.linkedNodes:
                self.linkedNodes[edge.departure].append(edge)
            else:
                self.linkedNodes[edge.departure] = [edge]

            if edge.destination in self.linkedNodes:
                self.linkedNodes[edge.destination].append(edge)
            else:
                self.linkedNodes[edge.destination] = [edge]

    def getTime(self, node1, node2):
        for edge in self.edges:
            if (edge.departure.number == node1 and edge.getDestination().number == node2) or (edge.departure.number == node2 and edge.getDestination().number == node1):
                return str(edge.getTime())

    def node(self, num):
        return self.nodes[int(num)-1]

    def plusCourtChemin(self, departure, destination):
        shortestDistance = {}
        predecessor = {}
        unseenNodes = self.linkedNodes  #faire une copie
        path = []
        infiniti = 99999

        for node in unseenNodes:
            shortestDistance[node] = infiniti
        shortestDistance[departure] = 0
        
        while unseenNodes:
            minNode = None
            for node in unseenNodes:
                if minNode is None:
                    minNode = node
                elif shortestDistance[node] < shortestDistance[minNode]:
                    minNode = node

        for childNode, weight in 
        