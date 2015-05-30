from tkinter import *

from game.Wolf import Wolf


class GUI:

    def __init__(self, master,world):
        #-MAIN WINDOW
        self.master = master
        master.title("Michal Martyniak 155136")
        master.resizable(0, 0)

#-FRAMES (Division main window by 2)
        self.lFrame = Frame(master, bg='black', width=600, height=600)
        self.lFrame.grid_propagate(False)

        self.pFrame = Frame(master, bg='white', width=500, height=500)
        self.pFrame.grid_propagate(False)

        self.lFrame.pack(side=LEFT)
        self.pFrame.pack(side=LEFT, fill='both')

#-2D array of labels initializing (each label is representing their owner)
        self.label = [[0 for x in range(20)] for y in range(20)]

        icon = PhotoImage(file='pusty.png')
        for y in range(20):
            for x in range(20):
                self.label[x][y] = Label(self.lFrame, image=icon, borderwidth=0)
                self.label[x][y].image = icon
                self.label[x][y].grid(row=y, column=x)

                #Hovering at labels puts Wolf in there :D
                def make_lambda(xx, yy, worldd):
                    return lambda event: self.insert(event, xx, yy, worldd)
                self.label[x][y].bind("<Enter>", make_lambda(x, y, world))

#-Buttons
        self.nextRun = Button(self.pFrame, text="Next round", bg='blue', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=107, pady=30)
        self.nextRun.bind("<Button-1>", lambda event: self.call_runoff(event, world))
        self.master.bind("<Return>", lambda event: self.call_runoff(event, world))
        self.nextRun.pack(side=TOP)
        #TODO BINDS for LOAD AND SAVE BUTTONS
        self.nextRun = Button(self.pFrame, text="Save", bg='orange', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=140, pady=30)
        self.nextRun.bind("<Button-1>")
        self.nextRun.pack(side=BOTTOM)

        self.nextRun = Button(self.pFrame, text="Load", bg='green', relief=RIDGE, cursor='dotbox', font='consolas', borderwidth=10, padx=140, pady=30)
        self.nextRun.bind("<Button-1>")
        self.nextRun.pack(side=BOTTOM)

    def insert(self, event, n, m, world):
        """insert wolf onto hovered label, just for fun"""
        img = PhotoImage(file='wolf.png')
        world.organism[n][m] = Wolf(n, m)
        self.label[n][m].configure(image=img)
        self.label[n][m].image = img

    def call_runoff(self, event, world):
        world.move_all()



