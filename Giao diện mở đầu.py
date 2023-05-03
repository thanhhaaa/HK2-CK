from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title = ("")
window.geometry = ("600x600")

mynotebook = ttk.Notebook(window)
mynotebook.pack()

def tab1():
    myframe = ttk.Frame(mynotebook)
    myframe.place(x=20,y=30)
    mynotebook.add(myframe, text="Kcal Calculator")
    but1 = Button(myframe, text='Quit', command=myframe.destroy)
    but1.pack(side=RIGHT)

def tab2():
    myframe = ttk.Frame(mynotebook)
    myframe.place(x=50, y=30)
    mynotebook.add(myframe, text="TDEE Calculator")
    but1 = Button(myframe, text='Quit', command=myframe.destroy)
    but1.pack(side=RIGHT)

bttn1 = Button(window, text="Kcal Calculator", command=tab1)
bttn1.pack()
bttn2 = Button(window, text="TDEE Calculator", command=tab2)
bttn2.pack()
window.mainloop()