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
