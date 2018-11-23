class Node:

    def __init__(self):
        self.nextState = {}
        self.finish = False

    def getNext(self, letter):
        return self.nextState[letter]

    def hasNext(self, letter):
        return letter in self.nextState

    def addNext(self, letter):
        self.nextState[letter] = Node()

    def next(self,letter):
        if not self.hasNext(letter):
            self.addNext(letter)
        return self.getNext(letter)

    def isEmpty(self):
        if self.nextState:
            return True
        else:
            return False

    def setFinish(self):
        self.finish=True

    def isFinished(self):
        return self.finish