class Edge:
    def __init__(self, node1, node2, time):
        self.node1 = node1
        self.node2 = node2
        self.time = time
    
    def getTemps(self):
        return self.time
    
    def getDeparture(self):
        return self.node1

    def getDestination(self):
        return self.node2