from edge import Edge

inf = float('inf')

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
        print(f"({key},  ({', '.join([f'({x.dest}, {x.time})' for x in edges])}))")

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


    def plusLongChemin(self, categorie, depart, destination):

        print(str(self.adjDict[1][2].time))
        distance = [inf]
        cheminInclut = [None]
        parent = [None]
        for node in self.adjDict:
            distance.append(inf)
            cheminInclut.append(False)
            parent.append(None)
        parent[1] = -1

        distance[depart] = 0

        for node in self.adjDict:

            min = inf
            minIndex = 1
            for key in self.adjDict:
                if cheminInclut[key] is False and distance[key] < min:
                    min = distance[key]
                    minIndex = key

            cheminInclut[minIndex] = True

            for i in self.adjDict:
                time = 0
                a = False
                for j in self.adjDict[minIndex]:
                    if (not cheminInclut[i] and i == j.dest
                            and distance[minIndex] + j.time < distance[i]):
                        a = True
                        time = j.time
                        parent[i] = minIndex
                        distance[i] = distance[minIndex] + time

        nouveauNodes = []
        src=1
        # print( "\n" + str(src) + "-> " + str(destination) + '\t' + str(distance[destination]))
        # self.printChemin(parent, destination)
        for i in self.adjDict:
            print("\n" + str(src) + "-> " + str(i) + '\t' + str(distance[i]))
            self.printChemin(parent, i)

    def printChemin(self, parent, j):

        if parent[j] == -1 or parent[j] == None:
            return;
        self.printChemin(parent,parent[j])
        print('->' + str(j))

    def extraireSousGraph(self,car,depart):
        self.plusLongChemin(1,int(depart),16)