from edge import Edge
from chemin import Chemin

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
        #affichage ordonnee pour le graph complet
        if max(self.adjDict.keys()) == 29 and min(self.adjDict.keys()) == 1:
            for key in range(min(self.adjDict.keys()),max(self.adjDict.keys())+1):
                self.printNode(key, self.adjDict[key])
        else:
            for key, edges in self.adjDict.items():
                self.printNode(key, edges)

    def printNode(self, key, edges):
        print(f"({key}, {int(edges[0].recharge)} ({', '.join([f'({x.dest}, {x.time})' for x in edges])}))")

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


    def plusCourtChemin(self, categorie, depart, destination):

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
        #self.plusCourtChemin(1,int(depart),16)

        self.plusLongChemin(1,80)

    def plusLongChemin(self,depart, drop):

        chemin = [depart]
        temps = 0
        energie = 100
        current = depart

        chemin, temps, energie, current = self.ajoutChemin(chemin, temps, energie, current, drop)

        print(f"(temps: {temps}, chemin: ({', '.join([f'({x})' for x in chemin])}))")

    def ajoutChemin(self, chemin, temps, energie, current, drop):
        plusGrandChemin = chemin + [current]
        tempsMax = temps
        nouvenergie = energie
        if not (energie < 20):
            for edge in self.adjDict[current]:
                if not edge.dest in chemin:
                    energie = energie - edge.time / 60 * drop
                    temps += edge.time
                    chemin.append(edge.dest)
                    current = edge.dest
                    nouvchemin, nouvtemps, nouvenergie, current = self.ajoutChemin(chemin, temps, energie, current, drop)
                    if tempsMax < nouvtemps:
                        plusGrandChemin = chemin
                        tempsMax = nouvtemps
                        print(tempsMax)
        return plusGrandChemin, tempsMax, nouvenergie, current