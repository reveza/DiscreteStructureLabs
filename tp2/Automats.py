from Node import Node

class Automates:
    def __init__(self, filename):
        self.start = Node()
        self.currentState = self.start
        self.words = {}
        self.readFile(filename)
        self.lastWords = []

    def readFile(self, filename):
        with open(filename) as file:
            for line in file:
                line = line.strip()
                self.words[line] = [0,0]
                self.currentState = self.start
                for letter in line:
                    if letter != '\n':
                        self.currentState = self.currentState.next(letter)
                self.currentState.setFinish()
            self.currentState = self.start

    def backToStart(self):
        self.currentState = self.start

    def nextNode(self, letter):
        self.currentState = self.currentState.next(letter)

    def print(self): #Pour vérifier que l'automate a bien marcher
        for letter in self.start.nextState.keys():
            print(letter)

    def printFromCurrentState(self, string):
        words = []
        self.printLetter(self.currentState, string, words)
        text = ""
        for mot in words:
            text += (mot + "\t\tused:" + str(self.words[mot][0]) + " last 5: " + ('yes' if self.words[mot][1] else 'no')  +"\n")
        return text

    def printLetter(self, node, string, words):
        for letter in node.nextState:
            stringtmp = string + letter
            if node.nextState[letter].isFinished():
                words.append(stringtmp)
            words = self.printLetter(node.nextState[letter], stringtmp, words)
        return words

    def resetLastFive(self):
        for mot in self.words:
            self.words[mot][1] = 0

    def incrementWordCount(self, word):
        if self.words.__contains__(word):
            self.words[word][0] += 1
            self.getLastFive(word)

    def getLastFive(self, word):
        self.lastWords.append(word)
        self.resetLastFive()
        for w in range(-5,0):
            if (-w) <= len(self.lastWords):
                self.words[self.lastWords[w]][1] = 1
