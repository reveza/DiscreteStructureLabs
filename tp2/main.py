from Automats import Automates
from GUI import GUI
from tkinter import *

#Note: avec le lexique 6, il faut un peu de temps pour que les mots s'affichent a la premiere lettre
auto = Automates("lexique5.txt")
auto.currentNode = auto.depart.next('a').next('m').next('i')
print(auto.printFromCurrentNode('ami'))
auto.currentNode = auto.depart

root = Tk()
root.geometry('200x200')
gui = GUI(root, auto)
gui.mainloop()