from Automats import Automates
from GUI import GUI
from tkinter import *

#Note: avec le lexique 6, il faut un peu de temps pour que les mots s'affichent a la premiere lettre
auto = Automates("lexique5.txt")
auto.currentState = auto.start.next('a').next('m').next('i')
print(auto.printFromCurrentState('ami'))
auto.currentState = auto.start

root = Tk()
root.geometry('300x300')
gui = GUI(root, auto)
gui.mainloop()