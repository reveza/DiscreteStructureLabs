from Node import Node

class Automates:

    def __init__(self, filename):
        self.depart = Node()
        self.currentNode = self.depart
        self.mots = {}
        self.readFile(filename)
        self.lastWords = []


    def readFile(self, filename):

        with open(filename) as file:
            for line in file:
                line = line.strip()
                self.mots[line] = [0,0]
                self.currentNode = self.depart
                for letter in line:
                    if letter != '\n':
                        self.currentNode = self.currentNode.next(letter)
                self.currentNode.setFinish()
            self.currentNode = self.depart

    def backToStart(self):
        self.currentNode = self.depart

    def nextNode(self, letter):
        self.currentNode = self.currentNode.next(letter)

    def print(self): #Pour vérifier que l'automate a bien marcher
        for letter in self.depart.nextLettres.keys():
            print(letter)

    def printFromCurrentNode(self, string):
        mots = []
        self.printLettre(self.currentNode, string, mots)
        text = ""
        for mot in mots:
            text += (mot + "\t\tused:" + str(self.mots[mot][0]) + " last 5: " + ('yes' if self.mots[mot][1] else 'no')  +"\n")
        return text

    def printLettre(self, node, string, mots):

        for next in node.nextLettres:
            stringtmp = string + next
            if node.nextLettres[next].getFinish():
                mots.append(stringtmp)
            mots = self.printLettre(node.nextLettres[next], stringtmp, mots)
        return mots

    def reset(self):
        for mot in self.mots:
            self.mots[mot][1] = 0

    def addCount(self, word):
        if self.mots.__contains__(word):
            self.mots[word][0] += 1
            self.lastFive(word)

    def lastFive(self, word):
        self.lastWords.append(word)
        self.reset()
        for w in range(-5,0):
            if (-w) <= len(self.lastWords):
                self.mots[self.lastWords[w]][1] = 1
