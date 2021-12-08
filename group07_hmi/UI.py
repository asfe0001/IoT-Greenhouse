from tkinter import*
from tkinter.ttk import*

root = Tk()
root.wm_title("Gewächshaus GUI")
root.config(background = "#FFFFFF")

luftFrame = Frame(root, width= 310, height = 125)
luftFrame.grid(row=0, column=0, padx=10, pady=3)
luftLabel = Label(luftFrame, text="Luftzustand")
luftLabel.grid(row=0, column=0, padx=10, pady=3)

bodenFrame = Frame(root, width= 310, height = 125)
bodenFrame.grid(row=1, column=0, padx=10, pady=3)
bodenLabel = Label(bodenFrame, text="Bodenzustand")
bodenLabel.grid(row=0, column=0, padx=10, pady=3)

wasserFrame = Frame(root, width= 310, height = 125)
wasserFrame.grid(row=2, column=0, padx=10, pady=3)
wasserLabel = Label(wasserFrame, text="Wasserzustand")
wasserLabel.grid(row=0, column=0, padx=10, pady=3)

lichtFrame = Frame(root, width= 310, height = 125)
lichtFrame.grid(row=3, column=0, padx=10, pady=3)
lichtLabel = Label(lichtFrame, text="Lichtzustand")
lichtLabel.grid(row=0, column=0, padx=10, pady=3)

luftReglerFrame = Frame(root, width= 310, height = 125)
luftReglerFrame.grid(row=0, column=1, padx=10, pady=3)

bodenReglerFrame = Frame(root, width= 310, height = 125)
bodenReglerFrame.grid(row=1, column=1, padx=10, pady=3)

wasserReglerFrame = Frame(root, width= 310, height = 125)
wasserReglerFrame.grid(row=2, column=1, padx=10, pady=3)

lichtReglerFrame = Frame(root, width= 310, height = 125)
lichtReglerFrame.grid(row=3, column=1, padx=10, pady=3)

luftEinheitFrame = Frame(root, width= 310, height = 125)
luftEinheitFrame.grid(row=0, column=2, padx=10, pady=3)

bodenEinheitFrame = Frame(root, width= 310, height = 125)
bodenEinheitFrame.grid(row=1, column=2, padx=10, pady=3)

wasserEinheitFrame = Frame(root, width= 310, height = 125)
wasserEinheitFrame.grid(row=2, column=2, padx=10, pady=3)

lichtEinheitFrame = Frame(root, width= 310, height = 125)
lichtEinheitFrame.grid(row=3, column=2, padx=10, pady=3)

root.mainloop()
