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

database.child("Rohan").set("Hello")