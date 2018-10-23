from sommet import Sommet
from arrete import Arrete


class Graph:

    def __init__(self, fileName):
        self.fileName = fileName
        self.sommets_read = []
        self.arretes_read = []
        self.sommets = []
        self.arretes = []

    def readFile(self):
        with open(self.fileName) as file:
            for line in file:
                if line != '\n':
                    words = [word.strip() for word in line.split(',')]
                    self.sommets_read.append(words)
                else:
                    break
            for line in file:
                self.arretes_read.append(
                    [word.strip() for word in line.split(',')]
                )
        file.close()
    
    def printGraph(self):
        for s in self.sommets:
            print('(sommet' + s.getNumber() +')')

    def createGraph(self):
        self.readFile()
        for s in self.sommets_read:
            sommet = Sommet(s[0], s[1])
            self.sommets.append(sommet)

        for a in self.arretes_read:
            sommet1 = int(a[0]) - 1
            sommet2 = int(a[1]) - 1
            time = int(a[2])
            arrete = Arrete(self.sommets[sommet1], self.sommets[sommet2], time)
            self.arretes.append(arrete)

    def adjacence(self,a,b):
        for s in self.arretes:
            if (s.departure == a & s.destination ==b) | (s.departure == b & s.destination ==a):
                return 1

    def trouverAdjacents(self, a):
        sommetsAdjacents = []
        arretesAdjacentes = []
        for s in self.sommets:
            if self.adjacence(self,a,s):
                sommetsAdjacents.append(s)
        return sommetsAdjacents

    def plusCourtChemin(self, origine, destination):
        assert origine in self.sommets

        distance = {sommet: inf for sommet in self.sommets}
        sommet_precedent = {sommet: None for sommet in self.sommets}
        distance[origine] = 0
        sommets = self.sommets.copy()

        while sommets:
            sommetActif = min(sommets, key=lambda sommet: distance[sommet])

            if distance[sommetActif] == inf:
                break;

            for adjacent, temps in self.adjacents[sommetActif]:
                route_alternative = distance[sommetActif] + temps

                if route_alternative < distance[adjacent]:
                    distance[adjacent] = route_alternative
                    sommet_precedent[adjacent] = sommetActif

            sommets.remove(sommetActif)

            pathS, sommetActif = deque(), destination
            while sommet_precedent[sommetActif] is not None:
                pathS.appendleft(sommetActif)
                sommetActif = sommet_precedent[sommetActif]
            if pathS:
                pathS.appendleft(sommetActif)
            return pathS
