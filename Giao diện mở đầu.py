from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

now = datetime.now()

window = Tk()
window.title("MANAGE DAILY CALORIE INTAKE ")
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
    myframe.place(x=20, y=30)
    mynotebook.add(myframe, text="Kcal Calculator")
    but1 = Button(myframe, text='Quit', command=myframe.destroy)
    but1.pack(side=RIGHT)
    mynotebook.select(myframe)


def tab2():
    myframe = ttk.Frame(mynotebook)
    myframe.place(x=50, y=30)
    mynotebook.add(myframe, text="TDEE Calculator")
    mynotebook.select(myframe)

    class TDEE_Class:
        def __init__(self, myframe, mynotebook):
            self.myframe = myframe
            self.mynotebook = mynotebook
            lb = Label(myframe, text="Calories per day", font=("courier bold", 25), bg="#E0FFFF")
            lb.pack(side=TOP, fill=X)

            self.var_height = StringVar()
            self.var_weight = StringVar()
            self.var_age = StringVar()
            self.var_workout = StringVar()
            self.var_gender = StringVar()
            self.var_yourTDEE = StringVar()

            lbl_age = Label(myframe, text="Age", font=("courier", 20), bg="#E0FFFF")
            lbl_age.pack()

            txt_age = Entry(myframe, textvariable=self.var_age, font=("Times", 15), bg="white")
            txt_age.pack()

            lbl_gender = Label(myframe, text="Gender", font=("courier", 20), bg="#E0FFFF")
            lbl_gender.pack()

            gender = ["Male", "Female"]
            rbt = ttk.Combobox(myframe, values=gender, textvariable=self.var_gender, font="Times 15")
            rbt.pack()

            lbl_height = Label(myframe, text="Height", font=("courier", 20), bg="#E0FFFF")
            lbl_height.pack()
            txt_height = Entry(myframe, textvariable=self.var_height, font=("Times", 15), bg="white")
            txt_height.pack()

            lbl_weight = Label(myframe, text="Weight", font=("courier", 20), bg="#E0FFFF")
            lbl_weight.pack()
            txt_weight = Entry(myframe, textvariable=self.var_weight, font=("Times", 15), bg="white")
            txt_weight.pack()

            lbl_workout = Label(myframe, text="Work out", font=("courier", 20), bg="#E0FFFF")
            lbl_workout.pack()
            workout = ["Inactive", "Light exercise (1-3 days/week)", "Average exercise (3-5 days/week)",
                       "Exercise a lot (6-7 days/week)", "High intensity exercise (everyday)"]
            Cmb = ttk.Combobox(myframe, values=workout, textvariable=self.var_workout, font="Times 15")
            Cmb.pack()

            btn_TDEE = Button(myframe, text=" Calculate TDEE", bg="#DCF8C6", command=self.TDEE, font=("Times", 14))
            btn_TDEE.pack()
            btn_clear = Button(myframe, text="Clear", bg="#BBBBBB", command=self.clear, font=("Times", 15))
            btn_clear.pack()

            lbl_your_TDEE = Label(myframe, text="Your TDEE", font=("courier", 20), bg="#E0FFFF")
            lbl_your_TDEE.pack()
            txt_your_TDEE = Entry(myframe, textvariable=self.var_yourTDEE, font=("Times", 20), bg="white",
                                  fg="#cc2900")
            txt_your_TDEE.pack()
            btn_exit = Button(myframe, text="Exit", fg="white", bg="#3B5988", command=self.exit,
                              font=("courier", 15))
            btn_exit.pack()

            note = Label(myframe, text="TDEE indicates the number of calories you need to eat in a day", font="Times 13")
            note.pack(side=BOTTOM, fill=X)

        def clear(self):
            self.var_age.set("")
            self.var_gender.set("")
            self.var_height.set("")
            self.var_weight.set("")
            self.var_workout.set("")
            self.var_yourTDEE.set("")

        def TDEE(self):
            self.g = (self.var_gender.get())
            if self.var_age.get() == "" or self.var_gender.get() == "" or self.var_height.get() == "" or self.var_weight.get() == "" or self.var_workout.get() == "":
                messagebox.showerror("Error", "Please enter full information")
            if self.g == "Male":
                self.a = int(self.var_age.get())
                self.h = float(self.var_height.get())
                self.w = float(self.var_weight.get())
                self.wk = (self.var_workout.get())
                self.number = round((self.w * 10) * 2.2046 + (self.h) * 6.25 * 0.39370 - (self.a * 5) + 5)
                if self.wk == "Inactive":
                    self.TDEE = round((self.number * 1.2), 2)
                if self.wk == "Light exercise (1-3 days/week)":
                    self.TDEE = round((self.number * 1.375), 2)
                if self.wk == "Average exercise (3-5 days/week)":
                    self.TDEE = round((self.number * 1.55), 2)
                if self.wk == "Exercise a lot (6-7 days/week)":
                    self.TDEE = round((self.number * 1.725), 2)
                if self.wk == "High intensity exercise (everyday)":
                    self.TDEE = round((self.number * 1.9), 2)
                self.var_yourTDEE.set(self.TDEE)
            elif self.g == "Female":
                self.a = int(self.var_age.get())
                self.h = float(self.var_height.get())
                self.w = float(self.var_weight.get())
                self.wk = (self.var_workout.get())
                self.number = round((self.w * 10) * 2.2 + (self.h) * 6.25 * 0.39 - (self.a * 5) - 161, 1)
                if self.wk == "Inactive":
                    self.TDEE = round((self.number * 1.2), 2)
                if self.wk == "Light exercise (1-3 days/week)":
                    self.TDEE = round((self.number * 1.375), 2)
                if self.wk == "Average exercise (3-5 days/week)":
                    self.TDEE = round((self.number * 1.55), 2)
                if self.wk == "Exercise a lot (6-7 days/week)":
                    self.TDEE = round((self.number * 1.725), 2)
                if self.wk == "High intensity exercise (everyday)":
                    self.TDEE = round((self.number * 1.9), 2)
                self.var_yourTDEE.set(self.TDEE)

        def exit(self):
            op = messagebox.askyesno("Confirm", "Do you want to leave this page?")
            if op == True:
                self.myframe.destroy()
    TDEE_Class(myframe, mynotebook)


def tab3():
    myframe = ttk.Frame(mynotebook)
    myframe.pack()
    mynotebook.add(myframe, text="Note")
    mynotebook.select(myframe)

    class Tab:
        def __init__(self, myframe, mynotebook):
            self.myframe = myframe
            self.mynotebook = mynotebook
            self.tab()

        def ghiFile(self, path, content):  # Lưu file
            f = open(path, "a", encoding="utf-8")
            f.write('-----' + now.strftime("%d") + "/" + now.strftime("%m") + "/" + now.strftime("%Y") + '-----' + "\n")
            f.write(content + "\n" + "\n")
            f.close()

        path = "run.txt"

        def tab(self):
            def save():
                inputValue = textbox.get("1.0", "end-1c")  # Lấy giá trị từ textbox
                self.ghiFile("run.txt", inputValue)
            textbox = Text(myframe, height=15)
            textbox.pack(fill=BOTH)
            but3 = Button(myframe, text='Quit', command=myframe.destroy, relief=GROOVE)
            but3.pack(side=RIGHT)
            but1 = Button(myframe, text="Save", command=save, relief=GROOVE)
            but1.pack(side=RIGHT)

    Tab(myframe, mynotebook)


abu = Text()
tab()
window.mainloop()
