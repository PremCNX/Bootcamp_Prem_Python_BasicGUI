#BasicGUI

from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.geometry('600x700')
GUI.title('โปรแกรมของ เปรม')

file = PhotoImage(file='durian.png')
IMG = Label(GUI,image=file,text='')
IMG.pack()


L1 = Label(GUI,text='โปรแกรมคำนวณทุเรียน',font = ('Cordia New',30,'bold'), fg = 'green')
L1.pack() #.place(x,y) .grid(row=)

L2 = Label(GUI,text='กรุณากรอกจำนวนทุเรียน',font= ('Cordia New',25))
L2.pack()

v_quantity = StringVar() 

E1 = ttk.Entry(GUI,textvariable = v_quantity,font=('Cordia New',20))
E1.pack()



def timestamp(thai=True):
	if thai == True:
		stamp = datetime.now()
		stamp = stamp.replace(year=stamp.year+543) #บวกเป็น พศ
		stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	else:
		stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	return stamp

def writetext (quantity,total):
	stamp = timestamp()
	filename = 'data.txt'
	with open(filename, 'a',encoding='utf-8') as file:
		file.write('\n' + 'วันเวลา: {} ทุเรียน: {} กิโลกรัม. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,total))

def writecsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) #fw = file writer
		fw.writerow(data)
	print('done')

def readcsv():
	with open('data.csv',newline='',encoding='utf-8') as file:
		fr = csv.reader(file)
		# print(list(fr))
		data = list(fr)
	return data

def sumdata():
	#ใช้สำหรับรวมค่าที่ได้จาก csv ไฟล์ ออกมาสองอย่าง
	result = readcsv()
	sumlist_quan = []
	sumlist_total = []
	for d in result:
		sumlist_quan.append(float(d[1]))
		sumlist_total.append(float(d[2]))
	sumquan = sum(sumlist_quan)
	sumtotal = sum(sumlist_total)
	
	return(sumquan,sumtotal)

def Calculate(event=None):
	quantity = v_quantity.get()
	price=100
	print ('จำนวณ', float(quantity) * price)
	cal = float(quantity)*price
	
	# writetext(quantity,cal)
	data = [timestamp(),quantity,cal]
	writecsv(data)

	title = 'ยอดที่ลูกค้าต้องจ่าย'
	text = 'ทุเรียนจำนวน {} กิโลกรัม ราคาทั้งหมด: {:,.2f} บาท'.format(quantity,cal)
	messagebox.showinfo(title,text)

	v_quantity.set('')#clear data
	E1.focus()

B1= ttk.Button(GUI, text='คำนวณ',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Calculate)

def SummaryData(event):
	#popup summary data
	sm = sumdata()
	title = 'ยอดสรุปรวมทั้งหมด'
	text = '\nจำนวนที่ขายได้: {} กิโลกรัม \nยอดขาย: {} บาท'.format(sm[0],sm[1])
	messagebox.showinfo(title,text)





GUI.bind('<F1>',SummaryData)
E1.focus() #ให้ cursur ไปยังตำแหน่งของ E1
GUI.mainloop()