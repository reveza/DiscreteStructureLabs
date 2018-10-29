from edge import Edge
import copy

# {
#     1: [Node(1,2,3,4), Node(1,3,4,5)],
#     2: [Node(2,8,3,4), Node(2,3,4,5)],
# }

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
        print(f"({key}, ({', '.join([f'({x.dest}, {x.time})' for x in edges])}))")
    
    def rebuildPath(self, source, destination, previous, energies):
        currPath = destination
        path = [currPath]
        energyFinal = energies[destination]

        while currPath != source:
            if previous[currPath] is not -1:
                currPath = previous[currPath]
                path.append(currPath)
            else:
                return False, None, None
        return True, path, energyFinal

    def dijkstra(self, source, energyDrop):
        times = {key: inf for key in self.adjDict.keys()}
        times[source] = 0
        previous = {key: -1 for key in self.adjDict.keys()}
        energies = {key: -1 for key in self.adjDict.keys()}
        energies[source] = 100
        rechargeTime = 0

        edges = set(self.adjDict.keys())

        while len(edges) > 0:
            current = min(edges, key=lambda edge: times[edge])
            print(f"Current {current} time: {times[current]}")
            edges.remove(current)

            for x in self.adjDict[current]:
                totalTime = times[current] + x.time
                tmpTime = times[x.dest]
                tmpPrev = previous[x.dest]
                if totalTime < times[x.dest]:
                    times[x.dest] = totalTime
                    previous[x.dest] = current

                    print(f"Time to dest: {times[x.dest]} from {x.dest}")

                    energyLost = (x.time / 60) * energyDrop

                    energyLeft = energies[current] - energyLost if energies[current] is not -1 else energies[source] - energyLost
                    print(energyLeft)
                    if energyLeft >= 20 :
                        energies[x.dest] = energies[current] - energyLost if energies[current] is not -1 else energies[source] - energyLost

                    elif energyLeft < 20 and x.recharge :
                        rechargeTime += 120
                        times[x.dest] += 120
                        energies[x.dest] = energies[source] - energyLost
                    
                    elif energyLeft < 20 and not x.recharge:
                        previous[x.dest] = tmpPrev
                        times[x.dest] = tmpTime
                        
        return energies, previous, times, rechargeTime

    def dijkstraNi(self, source, destination, risk):
        if risk == 'faible':
            energyDrop = 6
        if risk == 'moyen':
            energyDrop = 12
        if risk == 'eleve':
            energyDrop = 48

        energies, previous, times, rechargeTime = self.dijkstra(source, energyDrop)        

        isPossible, path, energyFinal = self.rebuildPath(source, destination, previous, energies)

        if not isPossible: 
            self.dijkstraLi(source, destination, risk)
        else:
            print(f"Vehicule: Ni, Recharge: {rechargeTime}, Energie finale: {energyFinal} , Temps: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")

    def dijkstraLi(self, source, destination, risk):
        if risk == 'faible':
            energyDrop = 5
        if risk == 'moyen':
            energyDrop = 10
        if risk == 'eleve':
            energyDrop = 30

        energies, previous, times, rechargeTime = self.dijkstra(source, energyDrop)

        isPossible, path, energyFinal = self.rebuildPath(source, destination, previous, energies)

        if not isPossible: 
            print('Voyage pas possible')
        else:
            print(f"Vehicule: Li, Recharge: {rechargeTime} Energie finale: {energyFinal}, Temps: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")
