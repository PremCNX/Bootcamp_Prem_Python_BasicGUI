#read json.py

import json

def readjson():
	with open('data.json',encoding='utf-8') as file:
		data = json.load(file)
		print(type(data))
		print(data[0])
	return data


def writejson(data):
	jsonobject = json.dumps(data,ensure_ascii=False,indent=4)
	with open('fruit.json','w',encoding='utf-8') as file:
		file.write(jsonobject)

data = {'1':['Banana',100,5],
		'2':['Durian',150,5],
		'3':['Apple',200,5],
		'4':['แก้วมังกร',300,5]}

writejson(data)
