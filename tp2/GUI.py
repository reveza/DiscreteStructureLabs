from tkinter import *
from Automats import Automates

class GUI(Frame):
    def __init__(self, master=None, graph = None):
        Frame.__init__(self, master)
        self.sv = StringVar()
        self.text = Text(self, width = 35)
        self.entry = Entry(self, textvariable = self.sv, width = 46)
        self.entry.bind("<KeyRelease>", self.on_entry)
        self.entry.bind('<Return>', self.on_enter)
        self.entry.pack(fill=X)
        self.pack()

        self.automates = graph

    def on_entry(self, event):
        wordsWrited = self.entry.get()
        self.automates.backToStart()
        words = wordsWrited.split(' ')[-1]

        for l in words:
            self.automates.nextNode(l)
        self.text.replace(1.0, END, self.automates.printFromCurrentNode(words))
        self.text.pack()

    def on_enter(self, event):
        wordsWrited = self.entry.get()
        words = wordsWrited.split(' ')
        for wor in words:
            self.automates.addCount(wor)
        self.entry.delete(0, END)