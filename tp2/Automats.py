from Node import Node

class Automates:

    def __init__(self, filename):
        self.depart = Node()
        self.currentNode = self.depart
        self.readFile(filename)

    def readFile(self, filename):

        with open(filename) as file:
            for line in file:
                self.currentNode = self.depart
                for letter in line:
                    self.currentNode = self.currentNode.next(letter)
            self.currentNode = self.depart

    def print(self): #Pour vérifier que l'automate a bien marcher
        for letter in self.depart.nextLettres.keys():
            print(letter)

    def printFromCurrentNode(self):
        self.printLettre(self.currentNode)

    def printLettre(self, node):
        for next in node.nextLettres:
            print(next)
            self.printLettre(node.nextLettres[next])