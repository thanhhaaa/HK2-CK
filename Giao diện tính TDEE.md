# HK2-CK
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

class TDEE_Class:
    def __init__(self,window):
        self.window=window
        self.window.title("Keep Fit")
        self.window.geometry("650x680+320+50")
        self.window.config(bg="#E0FFFF")
        self.window.resizable(width=False, height=False)
        self.window.title = Label(self.window, text="Calories per day",font =("courier bold",25),bg="#E0FFFF").pack(side=TOP,fill=X)

        

        self.var_height=StringVar()
        self.var_weight=StringVar()
        self.var_age=StringVar()
        self.var_workout=StringVar()
        self.var_gender = StringVar()
        self.var_yourTDEE=StringVar()


        lbl_age=Label(self.window,text="Age",font=("courier",20),bg="#E0FFFF")
        lbl_age.place(x=50,y=100)
        txt_age=Entry(self.window,textvariable=self.var_age,font=("Times",15),bg="white")
        txt_age.place(x=250,y=100,width=300,height=40)

        lbl_gender=Label(self.window,text="Gender",font=("courier",20),bg="#E0FFFF")
        lbl_gender.place(x=50,y=170)


        gender = ["Male","Female"]
        rbt = ttk.Combobox(self.window, values=gender, textvariable=self.var_gender, font="Times 15").place(x=250, y=170,width=300,height=40)

        lbl_height=Label(self.window,text="Height",font=("courier",20),bg="#E0FFFF")
        lbl_height.place(x=50,y=240)
        txt_height=Entry(self.window,textvariable=self.var_height,font=("Times",15),bg="white")
        txt_height.place(x=250,y=240,width=300,height=40)

        lbl_weight=Label(self.window,text="Weight",font=("courier",20),bg="#E0FFFF")
        lbl_weight.place(x=50,y=310)
        txt_weight=Entry(self.window,textvariable=self.var_weight,font=("Times",15),bg="white")
        txt_weight.place(x=250,y=310,width=300,height=40)

        lbl_workout=Label(self.window,text="Work out",font=("courier",20),bg="#E0FFFF").place(x=50,y=380)
        workout = ["Inactive", "Light exercise (1-3 days/week)", "Average exercise (3-5 days/week)",
                   "Exercise a lot (6-7 days/week)", "High intensity exercise (everyday)"]
        Cmb = ttk.Combobox(self.window,values=workout,textvariable=self.var_workout, font="Times 15").place(x=250,y=380,width=300,height=40)


        btn_TDEE=Button(self.window,text=" Calculate TDEE",bg="#DCF8C6",command=self.TDEE,font=("Times",14))
        btn_TDEE.place(x=250,y=430,width=160,height=50)
        btn_clear=Button(self.window,text="Clear",bg="#BBBBBB",command=self.clear,font=("Times",15))
        btn_clear.place(x=420,y=430,width=130,height=50)

        lbl_your_TDEE = Label(self.window, text="Your TDEE", font=("courier", 20), bg="#E0FFFF")
        lbl_your_TDEE.place(x=50, y=530)
        txt_your_TDEE = Entry(self.window,textvariable=self.var_yourTDEE, font=("Times", 20), bg="white",fg="#cc2900")
        txt_your_TDEE.place(x=250, y=530, width=300, height=40)


        btn_exit=Button(self.window,text="Exit",fg="white",bg="#3B5988",command=self.exit,font=("courier",15))
        btn_exit.place(x=300,y=590,width=130,height=50)

        note=Label(text="TDEE indicates the number of calories you need to eat in a day", font="Times 13")
        note.pack(side=BOTTOM, fill=X)

    def clear(self):
        self.var_age.set("")
        self.var_gender.set("")
        self.var_height.set("")
        self.var_weight.set("")
        self.var_workout.set("")
        self.var_yourTDEE.set("")


    def TDEE(self):
        self.g=(self.var_gender.get())
        if self.var_age.get()=="" or self.var_gender.get()=="" or self.var_height.get()=="" or self.var_weight.get()==""or self.var_workout.get()=="":
            messagebox.showerror("Error","Please enter full information")
        if self.g == "Male":
            self.a=int(self.var_age.get())
            self.h=float(self.var_height.get())
            self.w=float(self.var_weight.get())
            self.wk=(self.var_workout.get())
            self.number=round((self.w*10)*2.2046+(self.h)*6.25*0.39370-(self.a*5) +5)
            if self.wk == "Inactive":
                self.TDEE=round((self.number*1.2),2)
            if self.wk == "Light exercise (1-3 days/week)":
                self.TDEE=round((self.number*1.375),2)
            if self.wk == "Average exercise (3-5 days/week)":
                self.TDEE=round((self.number*1.55),2)
            if self.wk == "Exercise a lot (6-7 days/week)":
                self.TDEE=round((self.number*1.725),2)
            if self.wk == "High intensity exercise (everyday)":
                  self.TDEE=round((self.number*1.9),2)
            self.var_yourTDEE.set(self.TDEE)
        elif self.g == "Female":
            self.a=int(self.var_age.get())
            self.h=float(self.var_height.get())
            self.w=float(self.var_weight.get())
            self.wk=(self.var_workout.get())
            self.number=round((self.w*10)*2.2+(self.h)*6.25*0.39-(self.a*5) - 161,1)
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
        op=messagebox.askyesno("Confirm","Do you want to leave this page?")
        if op==True:
            self.window.destroy()

if __name__=="__main__":
    window =Tk()
    obj=TDEE_Class(window)
window.mainloop()
