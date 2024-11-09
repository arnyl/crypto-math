# Import the required libraries
from tkinter import *
from Params import gen_prime, generators, list_gen, setup
import random
from time import time
from random import choice

# Create an instance of tkinter frame or window
win=Tk()
win.title('User IPFE Setup')

# Set the size of the tkinter window
win.geometry("400x250")


def main_Setup():
    p = int(a.get())
    gens = generators(p)
    g = choice(gens)
    l = int(b.get())
    msk = list_gen(p, l) 
    mpk = setup(msk, g)
    label.config(text=mpk)
  
# Create an Entry widget
Label(win, text="Enter p", font=('Arial 10')).pack()
a=Entry(win, width=45)
a.pack()
Label(win, text="Enter l", font=('Arial 10')).pack()
b=Entry(win, width=45)
b.pack()

label=Label(win, text="Master Public Key: ", font=('Arial 11'))
label.pack(pady=25)

Button(win, text="Generate MPKey", command=main_Setup).pack()

win.mainloop()
