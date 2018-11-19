from Automats import Automates
from GUI import GUI
from tkinter import *

auto = Automates("lexique5.txt")
auto.currentNode = auto.depart.next('a').next('m').next('i')
print(auto.printFromCurrentNode('ami'))
auto.currentNode = auto.depart

root = Tk()
gui = GUI(root, auto)
gui.mainloop()