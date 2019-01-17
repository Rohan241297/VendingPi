# import RPi.GPIO as gp
import pyrebase
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

# print(database.child("items").child('1').child('name').get().val())

prevValue= database.child("items").child('1').child('prev').get().val()
# print(prevValue)

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
  if selected == 1:
    a,b=cokeData()
    if a !=0:
      print('Data Changed')
      database.child('items').child('1').child('prev').set(b)
  elif selected == 2:
    a,b=kitData()
    if a !=0:
      print('Data Changed')
      database.child('items').child('2').child('prev').set(b)
  elif selected == 3:
    a,b=supData()
    if a !=0:
      print('Data Changed')
      database.child('items').child('3').child('prev').set(b)
  elif selected == 4:
    a,b=laysData()
    if a !=0:
      print('Data Changed')
      database.child('items').child('4').child('prev').set(b)
  elif selected == 5:
    a,b=dairyData()
    if a !=0:
      print('Data Changed')
      database.child('items').child('5').child('prev').set(b)
    

  