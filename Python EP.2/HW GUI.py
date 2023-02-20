import tkinter as tk
from tkinter import messagebox




def show_message():
    text = 'เขามีเรื่องให้คิดเยอะ และนั่นไม่มีเรื่องของคุณอยู่เลยยย'
    messagebox.showinfo('ดอกไม้งาม',text)

root = tk.Tk()
root.title('วันนี้เขาคิดถึงคุณบ้างไหม')
root.geometry('800x1200')


img = tk.PhotoImage(file="Test1.png")


button = tk.Button(root, image=img, borderwidth=0,command=show_message)
button.pack(ipadx=2,ipady=2)
############
def show_message1():
    text = 'แอบคิดถึงนะ แต่ไม่แสดงออก'
    messagebox.showinfo('ดอกไม้งาม',text)

img1 = tk.PhotoImage(file="Test2.png")



button = tk.Button(root, image=img1, borderwidth=0,command=show_message1)
button.pack(ipadx=2,ipady=2)
############
def show_message2():
    text = 'คิดถึงคุณมากๆๆๆๆๆๆๆ เลยงับ'
    messagebox.showinfo('ดอกไม้งาม',text)

img2 = tk.PhotoImage(file="Test3.png")


button = tk.Button(root, image=img2, borderwidth=0,command=show_message2)
button.pack(ipadx=2,ipady=2)
############
def show_message3():
    text = 'คิดถึงคุณ คิดถึงทั้งวันนน'
    messagebox.showinfo('ดอกไม้งาม',text)

img3 = tk.PhotoImage(file="Test4.png")


button = tk.Button(root, image=img3, borderwidth=0,command=show_message3)
button.pack(ipadx=2,ipady=2)



root.mainloop()
