from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดหน้าจอ

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

##############
def Button2():
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='เงินมีกี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20) # กลางหน้าจอ
##############
def Button3():
    text = 'Python','Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20ี',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=100)
B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20) # กลางหน้าจอ





GUI.mainloop()
