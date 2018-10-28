from graph import Graph

menu = '(a) Mettre à jour la carte.\n(b) Déterminer le plus court chemin sécuritaire.\n'
menu += '(c) Extraire un sous-graphe.\n(d) Quitter.\n'
graph1 = Graph('centresLocaux.txt')
graph1.createGraph()
graph1.plusCourtChemin(1, 1, 15)

g = Graph("centresLocaux.txt")

# g.printGraph()
start = 1
destination = 23
g.dijkstra(start, destination)

# menu = '(a) Mettre a jour la carte.\n(b) Determiner le plus court chemin securitaire.\n'
# menu += '(c) Extraire un sous-graphe.\n(d) Quitter.\n'

# while True:
#     entree = input(menu)
#     if entree == 'a':
#         fichier = input('Entrer le nom du fichier: ')
#         graph1 = Graph('centresLocaux.txt')
#         graph1.createGraph()
#         graph1.printGraph()
#     elif entree == 'b':

#         condition = input('Entrer la condition du passager: \n(1) Risque faible \n(2) Risque moyen\n(3) Risque eleve')
#         depart = input('Entrer le point de depart: ')
#         desti = input('Entrer le point de destination: ')
#
#         graph1.plusCourtChemin(depart,desti)
#     elif entree == 'c':
#         sommet = input('Entrer le sommet de depart ')
#         while True:
#             car = input('Entrer le type de véhicule: \nN pour le NI-MH et L pour le LI-ion \n')
#             if car == 'L' or car == 'N':
#                 break
#             else:
#                 print('Mauvaise entree')
#

#         depart = input('Entrer le point de depart: ')
#         while True:
#             desti = input('Entrer le point de destination: ')
#             if desti == 'L' or desti == 'N':
#                 break
#             else:
#                 print('Mauvaise entree')
#         print(graph1.node(1))
#         graph1.plusCourtChemin(depart,desti)
#     elif entree == 'c':
#         sommet = input('Entrer le sommet de depart ')
#         car = input('Entrer le type de vehicule: \nN pour le NI-MH et L pour le LI-ion \n')

#     elif entree == 'd':
#         print('fin du programme')
#         break
#     else:
#         print('Entree invalide \n')
