from Node import Node
from Automats import Automates

auto = Automates("lexique5.txt")
auto.currentNode = auto.depart.next('c')
auto.printFromCurrentNode('c')