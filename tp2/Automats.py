from Node import Node

class Automates:

    def __init__(self, filename):
        self.depart = Node()
        self.currentNode = self.depart
        self.mots = []
        self.readFile(filename)


    def readFile(self, filename):

        with open(filename) as file:
            for line in file:
                line = line.strip()
                self.mots.append(line)
                self.currentNode = self.depart
                for letter in line:
                    if letter != '\n':
                        self.currentNode = self.currentNode.next(letter)
            self.currentNode = self.depart

    def print(self): #Pour vérifier que l'automate a bien marcher
        for letter in self.depart.nextLettres.keys():
            print(letter)

    def printFromCurrentNode(self, string):
        mots = []
        self.printLettre(self.currentNode, string, mots)
        for mot in mots:
            print(mot)

    def printLettre(self, node, string, mots):

        for next in node.nextLettres:
            stringtmp = string + next
            if self.mots.__contains__(stringtmp):
                mots.append(stringtmp)
            mots = self.printLettre(node.nextLettres[next], stringtmp, mots)
        return mots