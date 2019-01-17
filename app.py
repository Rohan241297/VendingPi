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

while True:
  prevValue= database.child("items").child('1').child('prev').get().val()
  presentValue=database.child("items").child('1').child('count').get().val()
  if prevValue-presentValue != 0:
    print('DataChanged')
    database.child("items").child("1").child("prev").set(presentValue)
  