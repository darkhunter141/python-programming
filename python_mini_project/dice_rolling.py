# import random module
import random
# import tkinter Package
from tkinter import *

# make an object
root = Tk()
# make the window
root.geometry("700x450")
# set the label and font size.
l1 = Label(root,text='', font=("times",200))

# define a function name roll
def roll():
    # take all the asci code for 1-6 numbers
    number = ['\u2680', '\u2681', '\u2682', '\u2683','\u2684','\u2685'  ]
    # take random number.
    l1.config(text=f'{random.choice(number)}')
    l1.pack()

# set the button and calling roll function on-click button
b1 = Button(root, text="Lets roll......", command=roll)
# set the button position
b1.place(x=330, y=0)

# looping window
root.mainloop()
