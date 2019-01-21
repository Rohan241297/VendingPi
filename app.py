import RPi.GPIO as gp
import pyrebase
import time
config = {
    'apiKey': "AIzaSyBJIreESnah74oUzVMy10VcUW-pX_4xiKM",
    'authDomain': "my-vending-machine.firebaseapp.com",
    'databaseURL': "https://my-vending-machine.firebaseio.com",
    'projectId': "my-vending-machine",
    'storageBucket': "my-vending-machine.appspot.com",
    'messagingSenderId': "148592097999"
  }
firebase = pyrebase.initialize_app(config)
database=firebase.database()
coke =3
kit =5
sup =7
lays =11
dairy = 13
sensor = 15
# print(prevValue)
gp.setmode(gp.BOARD)
gp.setup(coke,gp.OUT)
gp.setup(kit,gp.OUT)
gp.setup(sup,gp.OUT)
gp.setup(lays,gp.OUT)
gp.setup(dairy,gp.OUT)
gp.setup(sensor,gp.IN)
def cokeData():
	prevValue= database.child("items").child('1').child('prev').get().val()
	presentValue=database.child("items").child('1').child('count').get().val()
	return prevValue-presentValue,presentValue

def kitData():
	prevValue= database.child("items").child('2').child('prev').get().val()
	presentValue=database.child("items").child('2').child('count').get().val()
	return prevValue-presentValue,presentValue


def supData():
	prevValue= database.child("items").child('3').child('prev').get().val()
	presentValue=database.child("items").child('3').child('count').get().val()
	return prevValue-presentValue,presentValue

def laysData():
	prevValue= database.child("items").child('4').child('prev').get().val()
	presentValue=database.child("items").child('4').child('count').get().val()
	return prevValue-presentValue,presentValue

def dairyData():
	prevValue= database.child("items").child('5').child('prev').get().val()
	presentValue=database.child("items").child('5').child('count').get().val()
	return prevValue-presentValue,presentValue


while True:
	selected=database.child('selected').get().val()
	if gp.input(sensor)==1:
		database.child('received').set(1)
		time.sleep(2)
	else:
		database.child('received').set(0)
	if selected == 1:
		a,b=cokeData()
		if a !=0:
			#print('Data Changed')
			database.child('items').child('1').child('prev').set(b)
			gp.output(coke,1)
		else:
			gp.output(coke,0)
	elif selected == 2:
		a,b=kitData()
		if a !=0:
			#print('Data Changed')
			database.child('items').child('2').child('prev').set(b)
			gp.output(kit,1)
		else:
			gp.output(kit,0)
	elif selected == 3:
		a,b=supData()
		if a !=0:
			#print('Data Changed')
			database.child('items').child('3').child('prev').set(b)
			gp.output(sup,1)
		else:
			gp.output(sup,0)
	elif selected == 4:
		a,b=laysData()
		if a !=0:
			#print('Data Changed')
			database.child('items').child('4').child('prev').set(b)
			gp.output(lays,1)
		else:
			gp.output(lays,0)
	elif selected == 5:
		a,b=dairyData()
		if a !=0:
			#print('Data Changed')
			database.child('items').child('5').child('prev').set(b)
			gp.output(dairy,1)
		else:
			gp.output(dairy,0)

