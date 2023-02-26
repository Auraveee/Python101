#EP.4 eritefile.py

#########file text

def writedata():
    with open('data.txt','w',encoding='utf=8') as file:
        file.write('สวัสดี')

#บันทึกข้อมูลในไฟล์
#def adddata(text):
    #with open('add-data.txt','a',encoding='utf=8') as file:
        #file.writelines(text + '\n')

#adddata('วันที่ 04/02/2023 ลางานทั้งวัน')
#adddata('วันที่ 05/02/2023 ข้างานเวลา 08:30 น.')
#adddata('วันที่ 06/02/2023 ลางานทั้งวัน')


#########file csv

#บันทึกข้อมูลในไฟล์
def adddata(text):
    with open('add-data.txt','a',encoding='utf=8') as file:
        file.writelines(text + '\n')


def readdata():
    with open('add-data.txt',encoding='utf=8') as file:
        #data = file.readlines() #export to list
        data = file.read()
        print (data)

readdata()
