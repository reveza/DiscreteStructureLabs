from Graph import Graph

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
