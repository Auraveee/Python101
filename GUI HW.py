from tkinter import *
from tkinter import ttk
from tkinter import messagebox



GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('สุ่มดวง') # ชื่อโปรแกรม
GUI.geometry('500x400') # ขนาดหน้าจอ

L1 = Label(GUI,text='วันนี้เขาคิดถึงคุณบ้างไหม',font=('Angsana New',30),fg='green')
L1.place(x=30,y=20)

##############
def Button2():
    text = 'เขามีเรื่องให้คิดเยอะ และนั่นไม่มีเรื่องของคุณอยู่เลยยย'
    messagebox.showinfo('ดอกไม้งาม',text)

FB1 = Frame(GUI)
FB1.place(x=100,y=100)
B2 = ttk.Button(FB1,text='ดอกไม้งาม',command=Button2)
B2.pack(ipadx=20,ipady=20) # กลางหน้าจอ

##############
def Button3():
    text = 'แอบคิดถึงนะ แต่ไม่แสดงออก'
    messagebox.showinfo('แมวเหมียวอ้วน',text)

FB2 = Frame(GUI)
FB2.place(x=100,y=100)
B3 = ttk.Button(FB1,text='แมวเหมียวอ้วน',command=Button3)
B3.pack(ipadx=20,ipady=20) # กลางหน้าจอ

##############
def Button4():
    text = 'คิดถึงคุณมากๆๆๆๆๆๆๆ เลยงับ'
    messagebox.showinfo('เจ้าลูกหมาอ้วน',text)

FB3= Frame(GUI)
FB3.place(x=100,y=100)
B4 = ttk.Button(FB1,text='เจ้าลูกหมาอ้วน',command=Button4)
B4.pack(ipadx=20,ipady=20) # กลางหน้าจอ

##############
def Button5():
    text = 'คิดถึงคุณ คิดถึงทั้งวันนน'
    messagebox.showinfo('วาฬตัวใหญ่',text)

FB4= Frame(GUI)
FB4.place(x=100,y=100)
B5 = ttk.Button(FB1,text='วาฬตัวใหญ่',command=Button5)
B5.pack(ipadx=20,ipady=20) # กลางหน้าจอ





GUI.mainloop()
