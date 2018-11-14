from Node import Node

class Automates:

    def __init__(self, filename):
        self.depart = Node()
        self.currentNode = self.depart
        self.readFile(filename)

    def readFile(self, filename):

        with open(filename) as file:
            line = file.readline()
            for line in file:
                self.currentNode = self.depart
                for letter in line:
                    self.currentNode = self.currentNode.next(letter)

    def print(self):
        for letter in self.depart.nextLettres.keys():
            print(letter)


