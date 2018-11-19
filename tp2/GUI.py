from tkinter import *
from Automats import Automates

class GUI(Frame):
    def __init__(self, master=None, graph = None):
        Frame.__init__(self, master,width = 25, height = 20)
        self.sv = StringVar()
        self.text = Text(self, width = 20, height = 15)
        self.entry = Entry(self, textvariable = self.sv, width = 20)
        self.entry.bind("<KeyRelease>", self.on_entry)
        self.entry.pack()
        self.pack()

        self.automates = graph

    def on_entry(self, event):
        words = self.entry.get()
        self.automates.currentNode = self.automates.depart
        for l in words:
            self.automates.currentNode = self.automates.currentNode.next(l)
        self.text.replace(1.0, END, self.automates.printFromCurrentNode(words))
        self.text.pack()
