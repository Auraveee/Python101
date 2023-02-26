Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.

========= RESTART: /Users/auraveemala/Downloads/Python 101/writefile.py ========

5========= RESTART: /Users/auraveemala/Downloads/Python 101/writefile.py ========

5=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

5=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==
Traceback (most recent call last):
  File "/Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py", line 15, in <module>
    adddata('วันที่ 01/02/2023 ออกงานงานเวลา 17:30 น.')
  File "/Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py", line 12, in adddata
    file.writeline(text)
AttributeError: '_io.TextIOWrapper' object has no attribute 'writeline'. Did you mean: 'writelines'?

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

5=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==

5=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==
Traceback (most recent call last):
  File "/Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py", line 26, in <module>
    readdata()
  File "/Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py", line 22, in readdata
    with open('add-adta.txt',encoding='utf=8') as file:
FileNotFoundError: [Errno 2] No such file or directory: 'add-adta.txt'

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==
['โปรแกรมบันทึกเวลาเข้า-ออกงานวันที่ 01/02/2023 เข้างานเวลา 08:30 น.วันที่ 01/02/2023 ออกงานงานเวลา 17:30 น.วันที่ 02/02/2023 ลางานทั้งวัน\n', 'วันที่ 03/02/2023 ลางานทั้งวัน\n', 'วันที่ 04/02/2023 ลางานทั้งวัน\n', 'วันที่ 05/02/2023 ข้างานเวลา 08:30 น.\n', 'วันที่ 06/02/2023 ลางานทั้งวัน\n']

=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==
['โปรแกรมบันทึกเวลาเข้า-ออกงานวันที่ 01/02/2023 เข้างานเวลา 08:30 น.วันที่ 01/02/2023 ออกงานงานเวลา 17:30 น.วันที่ 02/02/2023 ลางานทั้งวัน\n', 'วันที่ 03/02/2023 ลางานทั้งวัน\n', 'วันที่ 04/02/2023 ลางานทั้งวัน\n', 'วันที่ 05/02/2023 ข้างานเวลา 08:30 น.\n', 'วันที่ 06/02/2023 ลางานทั้งวัน\n']
>>> 
=== RESTART: /Users/auraveemala/Downloads/Python 101/Python EP.4/writefile.py ==
โปรแกรมบันทึกเวลาเข้า-ออกงานวันที่ 01/02/2023 เข้างานเวลา 08:30 น.วันที่ 01/02/2023 ออกงานงานเวลา 17:30 น.วันที่ 02/02/2023 ลางานทั้งวัน
วันที่ 03/02/2023 ลางานทั้งวัน
วันที่ 04/02/2023 ลางานทั้งวัน
วันที่ 05/02/2023 ข้างานเวลา 08:30 น.
วันที่ 06/02/2023 ลางานทั้งวัน

>>> box = []
>>> box.append('วันที่ 04/02/2023')
>>> box.append('วันที่ 05/02/2023')
>>> box.append('วันที่ 06/02/2023')
>>> print(box)
['วันที่ 04/02/2023', 'วันที่ 05/02/2023', 'วันที่ 06/02/2023']
>>> print(box[1])
วันที่ 05/02/2023
>>> print (box[0])
วันที่ 04/02/2023
>>> print(box[-1])
วันที่ 06/02/2023
>>> print()box[-3]
SyntaxError: invalid syntax
>>> print(box[-3])
วันที่ 04/02/2023
>>> day = {'monday':['01/02/2023','08/02/2023'],'tuesday':['02/02/2023','09/02/2023']}
>>> print(day['monday'])
['01/02/2023', '08/02/2023']
>>> print (day['monday'][1])
08/02/2023
>>> print(day['tuesday'])
['02/02/2023', '09/02/2023']
>>> print(day['tuesday'][0])
02/02/2023
