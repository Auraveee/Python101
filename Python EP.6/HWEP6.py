class Milktea:
    #Attribute
    milkteaName = 'ชามนกูซู'

    #Constructor
    def __init__(self, subject='ชามนกูซู'):
        print('ร้านชานมกูซู')
        self.subject = subject

    #Method
    def hello(self):
        print('สวัสดีร้านชานมกูซู ยินดีตอนรับคุณลูกค้าทุกท่าน')

    def menu(self):
        print(f'เมนู {self.subject}')

class Menutea(Milktea):
    #Constructor
    def __init__(self, menuname, levelsweet, topping, size, subject):
        super().__init__(subject)
        self.menuname = menuname
        self.levelsweet = levelsweet
        self.topping = topping
        self.size = size

    #Method
    def checkPrice(self):
        if self.size >= 125:
            print(f'สินค้า {self.subject} ราคา 90')
        elif self.size >= 100:
            print(f'สินค้า {self.subject} ราคา 75')
        elif self.size >= 60:
            print(f'สินค้า {self.subject} ราคา 65')
        elif self.size >= 50:
            print(f'สินค้า {self.subject} ราคา 50')
        else:
            print(f'สินค้า {self.subject} ไม่มีสินค้า')


print('************************************')
milktea01 = Menutea('โกโก้', 75, 'ไข่มุก', 125, 'โกโก้')
milktea01.hello()
milktea01.menu()
print (f'ชื่อร้าน : {milktea01.milkteaName}')
print(f'ชื่อเมนู : {milktea01.menuname}')
print(f'ระดับความหวาน : {milktea01.levelsweet}')
print(f'Topping : {milktea01.topping}')
print(f'ขนาดแก้ว : {milktea01.size}')
milktea01.checkPrice()
print('************************************')
milktea02 = Menutea('ชานม', 25, 'ไม่ใส่ไข่มุก', 100, 'ชานม')
milktea02.hello()
milktea02.menu()
print (f'ชื่อร้าน : {milktea02.milkteaName}')
print(f'ชื่อเมนู : {milktea02.menuname}')
print(f'ระดับความหวาน : {milktea02.levelsweet}')
print(f'Topping : {milktea02.topping}')
print(f'ขนาดแก้ว : {milktea02.size}')
milktea02.checkPrice()
print('************************************')
milktea03 = Menutea('ชานม', 50, 'ไข่มุก', 50, 'ชานม')
milktea03.hello()
milktea03.menu()
print (f'ชื่อร้าน : {milktea03.milkteaName}')
print(f'ชื่อเมนู : {milktea03.menuname}')
print(f'ระดับความหวาน : {milktea03.levelsweet}')
print(f'Topping : {milktea03.topping}')
print(f'ขนาดแก้ว : {milktea03.size}')
milktea03.checkPrice()
print('************************************')
milktea04 = Menutea('ชาไทย', 100, 'ไม่ใส่ไข่มุก', 45, 'ชาไทย')
milktea04.hello()
milktea04.menu()
print (f'ชื่อร้าน : {milktea04.milkteaName}')
print(f'ชื่อเมนู : {milktea04.menuname}')
print(f'ระดับความหวาน : {milktea04.levelsweet}')
print(f'Topping : {milktea04.topping}')
print(f'ขนาดแก้ว : {milktea04.size}')
milktea04.checkPrice()
        
  


    
