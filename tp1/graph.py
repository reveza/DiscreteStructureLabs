from edge import Edge
import copy

# {
#     1: [Node(1,2,3,4), Node(1,3,4,5)],
#     2: [Node(2,8,3,4), Node(2,3,4,5)],
# }

inf = float('inf')

class Graph:

    def __init__(self, fileName = None):
        self.adjDict = {}
        if fileName != None:
            self.readFile(fileName)

    def createEdge(self, source, dest, time, recharge):
        edge = Edge(source, dest, time, recharge)
        if edge.source in self.adjDict:
            self.adjDict[edge.source].append(edge)
        else:
            self.adjDict[edge.source] = [edge]

    def readFile(self, fileName):
        nodes = {}
        with open(fileName) as file:
            line = file.readline()
            while line != "\n":
                words = [word.strip() for word in line.split(',')]
                nodes[int(words[0])] = words[1] == "1"
                line = file.readline()

            for line in file:
                words = [word.strip() for word in line.split(',')]
                source = int(words[0])
                dest = int(words[1])
                time = int(words[2])
                self.createEdge(source, dest, time, nodes[source])
                self.createEdge(dest, source, time, nodes[dest])
        file.close()

    def createGraph(self, chemin, times, recharges):
        for i in range(len(chemin)-1):
            self.createEdge(chemin[i], chemin[i+1], times[i], recharges[i])
            self.createEdge(chemin[i+1], chemin[i], times[i], recharges[i+1])

    def printGraph(self):
        # affichage ordonnee pour la visibilite
        for key in range(min(self.adjDict.keys()), max(self.adjDict.keys()) + 1):
            if key in self.adjDict.keys():
                self.printNode(key, self.adjDict[key])

    def printNode(self, key, edges):
        print(f"({key}, {int(edges[0].recharge)} ({', '.join([f'({x.dest}, {x.time})' for x in edges])}))")
    
    def rebuildPath(self, source, destination, previous, energies):
        currPath = destination
        path = [currPath]
        energyFinal = energies[destination]

        while currPath != source:
            if previous[currPath] is not -1:
                currPath = previous[currPath]
                path.append(currPath)
            else:
                return False, None, None
        return True, path, energyFinal

    def dijkstra(self, source, energyDrop):
        times = {key: inf for key in self.adjDict.keys()}           # mettre tous les temps à infini
        times[source] = 0                                           # le temps à l'origine est 0
        previous = {key: -1 for key in self.adjDict.keys()}
        energies = {key: -1 for key in self.adjDict.keys()}
        energies[source] = 100                                      # la batterie à l'origine est à 0
        rechargeTime = 0

        edges = set(self.adjDict.keys())

        while len(edges) > 0:
            current = min(edges, key=lambda edge: times[edge])      # on trouve le point le plus proche de l'origine
            edges.remove(current)                                   # on l'enlève car il est visité

            for x in self.adjDict[current]:                         # pour tous les sommets adjacents du somment courant
                totalTime = times[current] + x.time                 # on ajoute le temps entre l'adj et le somment courant au total
                tmpTime = times[x.dest]                             # ? valeur du temps avant de le changer a la ligne 90
                tmpPrev = previous[x.dest]                          # ? valeur de previous avant de le changer a la ligne 90
                if totalTime < times[x.dest]:                       # ? si le temps courrant + trajet node A vers B est plus petit que le temps des autres trajets pour se rendre au pointB
                    times[x.dest] = totalTime                       # ? remettre ce nouveau trajet comme etant le plus court (voila pourquoi on l'ajoute ds le vecteurs Times[node])
                    previous[x.dest] = current                      # ? idem pour previous.

                    energyLost = (x.time / 60) * energyDrop         # Calcul de l'énergie perdu dans le déplacement

                    energyLeft = energies[current] - energyLost if energies[current] is not -1 else energies[source] - energyLost  # Énergie restante                                                                                           # Sinon c'est la source moins la perte d'énergie
                    if energyLeft >= 20:                                                                                                        # Si l'énergie est en bas de 20%
                        energies[x.dest] = energies[current] - energyLost if energies[current] is not -1 else energies[source] - energyLost

                    elif energyLeft < 20 and x.recharge:                        # Si l'énergie est en bas de 20 et qu'il y a une borne de recharge
                        rechargeTime += 1                                       # On augmente le nombre de recharge
                        times[x.dest] += 120                                    # On prend en compte le temps de recharge
                        energies[x.dest] = energies[source] - energyLost        # ? EX: node A vers nodeB.  On recharge donc on repart avec une energie de 100% au nodeA (energie de la source), rendu au pt d'arrivee nodeB (dest), l'energie restante sera 100-energieDEpenserDuPointAauPointB 
                    
                    elif energyLeft < 20 and not x.recharge:                    # Si l'énergie est en bas de 20 et qu'il n'y a pas une borne de recharge
                        previous[x.dest] = tmpPrev                              # ? on avait change le previous a la ligne91, mais vu qu'on peut pas faire ce trajet, on ne veut pas l'ajouter comme etant un "bon" nouveau previous. donc on reaffecte la valeur precedente comme etant la meilleure.
                        times[x.dest] = tmpTime                                 # ? same que la ligne au dessu mais pr le temps
                        
        return energies, previous, times, rechargeTime

    def dijkstraNi(self, source, destination, risk):
        if risk == 'faible':
            energyDrop = 6
        elif risk == 'moyen':
            energyDrop = 12
        elif risk == 'eleve':
            energyDrop = 48
        else:
            print("Mauvaise entree")
            return

        energies, previous, times, rechargeTime = self.dijkstra(source, energyDrop)        

        isPossible, path, energyFinal = self.rebuildPath(source, destination, previous, energies)

        if not isPossible: 
            self.dijkstraLi(source, destination, risk)
        else:
            print(f"Vehicule: NI-NH, Recharge: {rechargeTime}, Energie restante: {int(energyFinal)} , Temps: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")

    def dijkstraLi(self, source, destination, risk):
        if risk == 'faible':
            energyDrop = 5
        elif risk == 'moyen':
            energyDrop = 10
        elif risk == 'eleve':
            energyDrop = 30
        else:
            print("Mauvaise entree")
            return

        energies, previous, times, rechargeTime = self.dijkstra(source, energyDrop)

        isPossible, path, energyFinal = self.rebuildPath(source, destination, previous, energies)

        if not isPossible: 
            print('Voyage pas possible')
        else:
            print(f"Vehicule: LI-ion, Recharge: {rechargeTime} Energie finale: {energyFinal}, Temps: {times[destination]} Path: {' -> '.join([str(x) for x in reversed(path)])}")

    def extraireSousGraph(self, depart, car, risk):

        chemin = []
        if car == 'NI-NH':
            if risk == 'faible':
                energyDrop = 6
            elif risk == 'moyen':
                energyDrop = 12
            elif risk == 'eleve':
                energyDrop = 48
            chemin = self.plusLongChemin(depart, energyDrop)
        elif car == 'LI-ion':
            if risk == 'faible':
                energyDrop = 5
            elif risk == 'moyen':
                energyDrop = 10
            elif risk == 'eleve':
                energyDrop = 30
            chemin = self.plusLongChemin(depart, energyDrop)
        else:
            print('Vehicule inexistant')
            return

        # Pour pouvoir creer un nouveau graph on a besoin des temps entre les sommets, et les recharges, qu'on obtient
        # des edges contenus dans le graph principale
        times = []
        recharges = []
        for i in range(len(chemin)-1):
            for edge in self.adjDict[chemin[i]]:
                if edge.dest == chemin[i+1]:
                    times.append(edge.time)
                    recharges.append(edge.recharge)
        recharges.append(self.adjDict[chemin[len(chemin)-1]][0].recharge) #obtenir la recharge sur le dernier element

        nouvGraph = Graph()
        nouvGraph.createGraph(chemin, times, recharges)
        nouvGraph.printGraph()
        return nouvGraph

    def plusLongChemin(self, depart, drop):

        chemin = []
        temps = 0
        energie = 100
        current = depart

        chemin, temps, energie, current = self.ajoutChemin(chemin, temps, energie, current, drop)

        print(f"(Temps: {temps}, chemin: ({', '.join([f'({x})' for x in chemin])}))")

        return chemin



    def ajoutChemin(self, chemin, temps, energie, current, drop):
        chemin = chemin + [current]
        plusGrandChemin = chemin
        tempsMax = temps
        energieMax = energie

        for edge in self.adjDict[current]:
            if not edge.dest in chemin:
                nouvenergie = energie - edge.time / 60 * drop
                if 20 < nouvenergie:
                    nouvtemps = temps + edge.time
                    current = edge.dest
                    nouvchemin, nouvtemps, nouvenergie, current = self.ajoutChemin(chemin, nouvtemps, nouvenergie, current,
                                                                               drop)
                    if tempsMax < nouvtemps:
                        plusGrandChemin = nouvchemin
                        tempsMax = nouvtemps
                        energieMax = nouvenergie

        return plusGrandChemin, tempsMax, energieMax, current