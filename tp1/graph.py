from Edge import Edge
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

        currPath = destination
        path = [currPath]
        while currPath != source:
            currPath = previous[currPath]
            path.append(currPath)

        print(f"Cost: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")
