from graph import Graph

menu = '(a) Mettre à jour la carte.' + '\n' + '(b) Déterminer le plus court chemin sécuritaire.' + '\n'
menu += '(c) Extraire un sous-graphe.' + '\n' + '(d) Quitter.'
while True:
    entree = input(menu)
    if entree == 'a':
        fichier = input('Entrer le nom du fichier: ')
        graph1 = Graph('centresLocaux.txt')
        graph1.createGraph()
        graph1.printGraph()
    elif entree == 'b':
        print(graph1.node(1))
        graph1.plusCourtChemin()
    elif entree == 'c':
        rin = input()
    elif entree == 'd':
        print('fin du programme')
        break
    else:
        print('entree invalide')
