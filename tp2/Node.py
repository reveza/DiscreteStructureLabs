class Node:

    def __init__(self):
        self.nextLettres = {}

    def getNext(self, lettre):
        return self.nextLettres[lettre]

    def hasNext(self, lettre):
        return lettre in self.nextLettres

    def addNext(self, lettre):
        self.nextLettres[lettre] = Node()

    def next(self,letter):
        if not self.hasNext(letter):
            self.addNext(letter)
        return self.getNext(letter)

    def isEmpty(self):
        if self.nextLettres:
            return True
        else:
            return False
