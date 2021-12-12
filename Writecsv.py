#writecsv.py
import csv

def writecsv(data):
	with open('data.csv','a',newline='',encoding='utf-8') as file:
		fw = csv.writer(file) #fw = file writer
		fw.writerow(data)
	print('done')

# d = ['2021-05-11 10:15:10',50,5000]

# writecsv(d)


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

result = sumdata()
print(result)




result = readcsv()
# print(result)

sumlist_quan = []
for d in result:
	sumlist_quan.append(float(d[1]))

print(sumlist_quan), sum(sumlist_quan)


sumlist_quan2 = sum ([float(d[1]) for d in result])
print(sumlist_quan2)





