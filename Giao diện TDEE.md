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

        self.window.title = Label(self.window, text="Lượng calories mỗi ngày",font =("courier bold",25),bg="#E0FFFF").pack(side=TOP,fill=X)

        self.var_height=StringVar()

        self.var_weight=StringVar()

        self.var_age=StringVar()

        self.var_workout=StringVar()

        self.var_gender = StringVar()

        self.var_yourTDEE=StringVar()

        lbl_age=Label(self.window,text="Tuổi",font=("courier",20),bg="#E0FFFF")

        lbl_age.place(x=50,y=100)

        txt_age=Entry(self.window,textvariable=self.var_age,font=("Times",15),bg="white")

        txt_age.place(x=250,y=100,width=300,height=40)

        lbl_gender=Label(self.window,text="Giới tính",font=("courier",20),bg="#E0FFFF")

        lbl_gender.place(x=50,y=170)

        gender = ["Nam","Nữ"]

        rbt = ttk.Combobox(self.window, values=gender, textvariable=self.var_gender, font="Times 15").place(x=250, y=170,width=300,height=40)

        lbl_height=Label(self.window,text="Chiều cao",font=("courier",20),bg="#E0FFFF")

        lbl_height.place(x=50,y=240)

        txt_height=Entry(self.window,textvariable=self.var_height,font=("Times",15),bg="white")

        txt_height.place(x=250,y=240,width=300,height=40)

        lbl_weight=Label(self.window,text="Cân nặng",font=("courier",20),bg="#E0FFFF")

        lbl_weight.place(x=50,y=310)

        txt_weight=Entry(self.window,textvariable=self.var_weight,font=("Times",15),bg="white")

        txt_weight.place(x=250,y=310,width=300,height=40)

        lbl_workout=Label(self.window,text="Vận động",font=("courier",20),bg="#E0FFFF").place(x=50,y=380)

        workout = ["Không hoạt động", "Hoạt động nhẹ (tập luyện 1-3 ngày/tuần)", "Hoạt động trung bình (tập luyện 3-5 ngày/tuần)",

                   "Hoạt động nặng (tập luyện 6-7 ngày/tuần)", "Hoạt động rất nặng (tập luyện nhiều hơn 7 ngày/tuần"]

        Cmb = ttk.Combobox(self.window,values=workout,textvariable=self.var_workout, font="Times 15").place(x=250,y=380,width=300,height=40)

        btn_TDEE=Button(self.window,text="Tính TDEE",bg="#DCF8C6",command=self.TDEE,font=("courier",15))

        btn_TDEE.place(x=250,y=430,width=130,height=50)

        btn_clear=Button(self.window,text="Xóa",bg="#BBBBBB",command=self.clear,font=("Times",15))

        btn_clear.place(x=420,y=430,width=130,height=50)

        lbl_your_TDEE = Label(self.window, text="TDEE của bạn là", font=("courier", 20), bg="#E0FFFF")

        lbl_your_TDEE.place(x=50, y=530)

        txt_your_TDEE = Entry(self.window,textvariable=self.var_yourTDEE, font=("Times", 20), bg="white",fg="#cc2900")

        txt_your_TDEE.place(x=250, y=530, width=300, height=40)

        btn_exit=Button(self.window,text="Exit",fg="white",bg="#3B5988",command=self.exit,font=("courier",15))

        btn_exit.place(x=300,y=590,width=130,height=50)

        note=Label(text="TDEE cho biết số lượng calories bạn cần ăn trong một ngày", font="Times 13")

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

            messagebox.showerror("Lỗi","Vui lòng nhập đầy đủ thông tin")

        if self.g == "Nam":

            self.a=int(self.var_age.get())

            self.h=float(self.var_height.get())

            self.w=float(self.var_weight.get())

            self.wk=(self.var_workout.get())

            self.number=round((self.w*10)*2.2046+(self.h)*6.25*0.39370-(self.a*5) +5)

            if self.wk == "Không hoạt động":

                self.TDEE=round((self.number*1.2),2)

            if self.wk == "Hoạt động nhẹ (tập luyện 1-3 ngày/tuần)":

                self.TDEE=round((self.number*1.375),2)

            if self.wk == "Hoạt động trung bình (tập luyện 3-5 ngày/tuần)":

                self.TDEE=round((self.number*1.55),2)

            if self.wk == "Hoạt động nặng (tập luyện 6-7 ngày/tuần)":

                self.TDEE=round((self.number*1.725),2)

            if self.wk == "Hoạt động rất nặng (tập luyện nhiều hơn 7 ngày/tuần)":

                  self.TDEE=round((self.number*1.9),2)

            self.var_yourTDEE.set(self.TDEE)

        elif self.g == "Nữ":

            self.a=int(self.var_age.get())

            self.h=float(self.var_height.get())

            self.w=float(self.var_weight.get())

            self.wk=(self.var_workout.get())

            self.number=round((self.w*10)*2.2+(self.h)*6.25*0.39-(self.a*5) - 161,1)

            if self.wk == "Không hoạt động":

                self.TDEE = round((self.number * 1.2), 2)

            if self.wk == "Hoạt động nhẹ (tập luyện 1-3 ngày/tuần)":

                self.TDEE = round((self.number * 1.375), 2)

            if self.wk == "Hoạt động trung bình (tập luyện 3-5 ngày/tuần)":

                self.TDEE = round((self.number * 1.55), 2)

            if self.wk == "Hoạt động nặng (tập luyện 6-7 ngày/tuần)":

                self.TDEE = round((self.number * 1.725), 2)

            if self.wk == "Hoạt động rất nặng (tập luyện nhiều hơn 7 ngày/tuần)":

                self.TDEE = round((self.number * 1.9), 2)

            self.var_yourTDEE.set(self.TDEE)

    def exit(self):

        op=messagebox.askyesno("Xác nhận","Bạn có muốn thoát khỏi trang này không?")

        if op==True:

            self.window.destroy()

if __name__=="__main__":

    window =Tk()

    obj=TDEE_Class(window)

window.mainloop()
