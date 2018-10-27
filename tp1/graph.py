from node import Node
from edge import Edge
from collections import deque
import copy

inf = float('inf')

class Graph:

    def __init__(self, filename = None, nodes = None, edges = None):

        self.fileName = filename;
        if nodes==None:
            self.nodes = []
        else:
            self.nodes=nodes
        if edges ==None:
            self.edges = []
        else:
            self.edges=edges
        self.linkedNodes = {}


    def createNode(self, numero, recharge):
        node = Node(numero, recharge)
        self.nodes.append(node)
    
    def createEdge(self, node1, node2, time):
        edge = Edge(self.nodes[node1], self.nodes[node2], time)
        self.edges.append(edge)

    def readFile(self,):
        with open(self.fileName) as file:
            for line in file:
                if 2 < len(line):
                    words = [word.strip() for word in line.split(',')]
                    self.createNode(int(words[0]), int(words[1]))
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
            string = '('
            string += str(i) + ', ' + str(self.node(i).getRecharge()) + ', ('
            for j in self.linkedNodes[i]:
                string += ('(' + str(j) + ', ' + str(self.getTime(i, j))) + '), '
            string = string[:-2] + '))'
            print(string)


    def createGraph(self):
        if self.fileName != None:
            self.readFile()
        for edge in self.edges:
            if edge.getDeparture().getNumber() in self.linkedNodes:
                self.linkedNodes[edge.getDeparture().getNumber()].append(int(edge.getDestination().getNumber()))
            else:
                self.linkedNodes[edge.getDeparture().getNumber()] = [edge.getDestination().getNumber()]
            if edge.getDestination().getNumber() in self.linkedNodes:
                self.linkedNodes[edge.getDestination().getNumber()].append(int(edge.getDeparture().getNumber()))
            else:
                self.linkedNodes[edge.getDestination().getNumber()] = [int(edge.getDeparture().getNumber())]


    def getTime(self, node1, node2):
        for edge in self.edges:
            if (edge.getDeparture().getNumber() == node1 and edge.getDestination().getNumber() == node2) or (edge.getDeparture().getNumber() == node2 and edge.getDestination().getNumber() == node1):
                print(edge.getTime())
                return edge.getTime()

    def getNode(self, num):
        return self.nodes[num-1]

    def plusCourtChemin(self, departure, destination):

        # distance = {node: inf for node in self.linkedNodes}
        # lastNode = {node: None for node in self.linkedNodes}

        distance = []
        lastNode = []

        for node in self.linkedNodes:
            distance.append(inf);
            lastNode.append(None);

        distance[departure-1] = 0;
        nodes = copy.deepcopy(self.linkedNodes)

        # neighbor.getNumber()  self.getTime(currentNode, neighbor))

        while nodes:

            minDistance = min(distance);
            currentNode = distance.index(minDistance);

            if distance[currentNode] == inf:
                break

            for currentNode in nodes:
                for neighbor in nodes[currentNode]:
                    intCurrentNode = int(currentNode)
                    node1 = self.getNode(intCurrentNode)
                    node2 = self.getNode(neighbor)

                    print(self.getNode(neighbor))
                    print(neighbor)
                    print(intCurrentNode)
                    print(self.getTime(node1, node2))

                    alternativePath = distance[intCurrentNode-1] + self.getTime(neighbor, intCurrentNode)
                    # print(self.getTime(node(currentNode), node(neighbor)))

                    if alternativePath < distance[neighbor-1]:
                        distance[neighbor-1] = alternativePath
                        lastNode[neighbor-1] = currentNode

            del nodes[currentNode]

            pathS, currentNode = deque(), destination
            while lastNode[currentNode] is not None:
                pathS.appendleft(currentNode)
                currentNode = lastNode[currentNode]
            if pathS:
                pathS.appendleft(currentNode)
            print(pathS)

    def extraireSousGraphe(self, root, type):

        return