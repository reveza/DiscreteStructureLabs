from graph import Graph

menu = '(a) Mettre à jour la carte.\n(b) Déterminer le plus court chemin sécuritaire.\n'
menu += '(c) Extraire un sous-graphe.\n(d) Quitter.\n'
while True:
    entree = input(menu)
    if entree == 'a':
        fichier = input('Entrer le nom du fichier: ')
        graph1 = Graph('centresLocaux.txt')
        graph1.createGraph()
        graph1.printGraph()
    elif entree == 'b':
        depart = input('Entrer le point de depart: ')
        while True:
            desti = input('Entrer le point de destination: ')
            if desti == 'L' or desti == 'N':
                break
            else:
                print('Mauvaise entree')
        print(graph1.node(1))
        graph1.plusCourtChemin(depart,desti)
    elif entree == 'c':
        sommet = input('Entrer le sommet de depart ')
        car = input('Entrer le type de véhicule: \nN pour le NI-MH et L pour le LI-ion \n')
    elif entree == 'd':
        print('fin du programme')
        break
    else:
        print('Entree invalide \n')
