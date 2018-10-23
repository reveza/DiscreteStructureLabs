class Arrete:
    def __init__(self, sommet1, sommet2, time):
        self.sommet1 = sommet1
        self.sommet2 = sommet2
        self.time = time
    
    def getTemps(self):
        return self.time
    
    def departure(self):
        return self.sommet1

    def destination(self):
        return self.sommet2