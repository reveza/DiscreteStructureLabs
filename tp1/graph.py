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
        for i in range(1, len(self.nodes)):
             self.linkedNodes[i] = []
        for edge in self.edges:
            if edge.getDeparture().getNumber() in self.linkedNodes:
                self.linkedNodes[edge.getDeparture().getNumber()].append(edge.getDestination().getNumber())
            else:
                self.linkedNodes[edge.getDeparture().getNumber()] = [edge.getDestination().getNumber()]
            if edge.getDestination().getNumber() in self.linkedNodes:
                self.linkedNodes[edge.getDestination().getNumber()].append(edge.getDeparture().getNumber())
            else:
                self.linkedNodes[edge.getDestination().getNumber()] = [edge.getDeparture().getNumber()]


    def getTime(self, node1, node2):
        for edge in self.edges:
            if (edge.getDeparture().getNumber() == node1 and edge.getDestination().getNumber() == node2) or (edge.getDeparture().getNumber() == node2 and edge.getDestination().getNumber() == node1):
                return edge.getTime()

    def node(self, num):
        return self.nodes[int(num)-1]

    def djikstraLong(self, categorie, depart, destination):

        distance = [inf]
        cheminInclut = [None]
        parent = [None]
        for node in self.linkedNodes:
            distance.append(inf)
            cheminInclut.append(False)
            parent.append(None)
        parent[0] = -1

        distance[depart] = 0

        for node in self.linkedNodes:

            min = inf
            minIndex = 1
            for key in self.linkedNodes:
                if cheminInclut[key] is False and distance[key] < min:
                    min = distance[key]
                    minIndex = key

            cheminInclut[minIndex] = True

            for i in self.linkedNodes:

                if (not cheminInclut[i] and i in self.linkedNodes[minIndex] and
                        distance[minIndex] + self.getTime(minIndex, i) < distance[i]):
                    parent[i] = minIndex
                    distance[i] = distance[minIndex] + self.getTime(minIndex, i)
        nouveauNodes = []
        src=1
        print( "\n" + str(src) + "-> " + str(destination) + '\t' + str(distance[destination]))
        self.printChemin(parent, destination)

    def printChemin(self, parent, j):

        if parent[j] == -1 or parent[j] == None:
            return;
        self.printChemin(parent,parent[j])
        print('->' + str(j))
        
    def plusCourtChemin(self, departure, destination):

        # distance = {node: inf for node in self.linkedNodes}
        # lastNode = {node: None for node in self.linkedNodes}

        distance = []
        lastNode = []

        for node in self.linkedNodes:
            distance.append(inf);
            lastNode.append(None);

        distance[departure] = 0;
        node = copy.deepcopy(self.linkedNodes)

        # neighbor.getNumber()  self.getTime(currentNode, neighbor))

        while node:

            currentNode = min(distance)

            if distance[distance.index(currentNode)] == inf:
                break

            for currentNode in node:
                for neighbor in node[currentNode]:
                    alternativePath = distance[distance.index(currentNode)] + self.getTime(node(currentNode), node(neighbor))
                    # print(self.getTime(node(currentNode), node(neighbor)))

                if alternativePath < distance[neighbor]:
                    distance[neighbor] = alternativePath
                    lastNode[neighbor] = currentNode

            node.remove(currentNode)

            pathS, currentNode = deque(), destination
            while lastNode[currentNode] is not None:
                pathS.appendleft(currentNode)
                currentNode = lastNode[currentNode]
            if pathS:
                pathS.appendleft(currentNode)
            print(pathS)

    def extraireSousGraphe(self, root, type):

        return