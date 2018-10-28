from edge import Edge
import copy

# {
#     1: [Node(1,2,3,4), Node(1,3,4,5)],
#     2: [Node(2,8,3,4), Node(2,3,4,5)],
# }
class Graph:

    def __init__(self, fileName):
        self.adjDict = {}
        self.readFile(fileName)

    def createEdge(self, source, dest, time, recharge):
        edge = Edge(source, dest, time, recharge)
        if edge.source in self.adjDict:
            self.adjDict[edge.source].append(edge)
        else:
            self.adjDict[edge.source] = [edge]

    def readFile(self, fileName):
        nodes = {}
        with open(fileName) as file:
            line = file.readline()
            while line != "\n":
                words = [word.strip() for word in line.split(',')]
                nodes[int(words[0])] = words[1] == "1"
                line = file.readline()

            for line in file:
                words = [word.strip() for word in line.split(',')]
                source = int(words[0])
                dest = int(words[1])
                time = int(words[2])
                self.createEdge(source, dest, time, nodes[source])
                self.createEdge(dest, source, time, nodes[dest])
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

    def printGraph(self):
        for key, edges in self.adjDict.items():
            self.printNode(key, edges)


    def printNode(self, key, edges):
        print(f"({key}, {'(, '.join([f'({x.dest}, {x.time})' for x in edges])})")

    def dijkstra(self, source, destination):
        times = {key: 9999 for key in self.adjDict.keys()}
        previous = {key: -1 for key in self.adjDict.keys()}

        times[source] = 0
        edges = set(self.adjDict.keys())

        while len(edges) > 0:
            current = min(edges, key=lambda edge: times[edge])
            print(f"Current {current} time: {times[current]}")
            edges.remove(current)

            for x in self.adjDict[current]:
                if times[current] + x.time < times[x.dest]:
                    times[x.dest] = times[current] + x.time
                    previous[x.dest] = current
                    print(f"Time to dest: {times[x.dest]} from {x.dest}")

        currPath = destination
        path = [currPath]
        while currPath != source:
            currPath = previous[currPath]
            path.append(currPath)

        print(f"Cost: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")
