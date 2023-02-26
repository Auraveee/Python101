from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#############################CSV###########################
import csv

def writecsv(datalist):
    with open('data.csv', 'a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist)

def readcsv():
    with open('data.csv', encoding='utf-8',newline='') as file:
        fr = csv.reader(file) #fw = file reader
        data = list(fr)
    return data 

#############################CSV###########################




GUI = Tk() # หน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') # ชื่อโปรแกรม
GUI.geometry('900x400') # ขนาดหน้าจอ

L1 = Label(GUI,text='โปรแกรมบันทึกรายรับ - รายจ่ายประจำเดือน',font=('Angsana New',30),fg='green')
L1.place(x=180,y=20)

##############

##############SECTION RIGHT##################
LF1 = ttk.LabelFrame(GUI,text='กรอกข้อมูลรายรับ - รายจ่าย')
LF1.place(x=2850,y=90)

v_data = StringVar() # ตัวแปรพิเศษที่ใช้กับข้อความใน gui
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',25))
E1.pack(pady=10,padx=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [t,data] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

B4 = ttk.Button(LF1,text='บันทึก',command=SaveData)
B4.pack(ipadx=20,ipady=20)

GUI.mainloop()
