from datetime import datetime


def writetext (qualtity,total)
	#EN DATE
	#stamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
	#THAI DATE
	stamp = datetime.now()
	stamp = stamp.replace(year=stamp.year+543) #บวกเป็น พศ
	stamp = stamp.strftime('%Y-%m-%d %H:%M:%S')
	filename = 'data.txt'
	with open(filename, 'a',encoding='utf-8') as file:
		file.write('\n' + 'วันเวลา: {} ทุเรียน: {} กิโลกรัม. รวมยอดทั้งหมด: {:,.2f} บาท'.format(stamp,quantity,cal))