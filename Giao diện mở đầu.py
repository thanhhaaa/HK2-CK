from tkinter import *
from tkinter import ttk
from tkinter.ttk import *

window = Tk()
window.title = ("")
window.geometry("600x300")

mynotebook = ttk.Notebook(window)
mynotebook.pack(fill=BOTH)


def tab():
    myframe = ttk.Frame(mynotebook)
    myframe.pack(fill=BOTH)
    mynotebook.add(myframe, text="Trang chủ")
    mylabel = Label(myframe, text='Choose feature:')
    mylabel.pack(fill=BOTH, expand=1)
    bttn1 = Button(myframe, text="Kcal Calculator", command=tab1, width=15)
    bttn1.pack(side=LEFT)
    bttn2 = Button(myframe, text="TDEE Calculator", command=tab2, width=15)
    bttn2.pack(side=LEFT)
    bttn3 = Button(myframe, text="Note", command=tab3, width=15)
    bttn3.pack(side=LEFT)

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

def tab3():
    myframe = ttk.Frame(mynotebook)
    myframe.pack()
    mynotebook.add(myframe, text="Note")
    but1 = Button(myframe, text='Quit', command=myframe.destroy)
    but1.pack(side=RIGHT)



abu = Text()
tab()
window.mainloop()