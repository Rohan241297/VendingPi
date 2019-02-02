import RPi.GPIO as gp
import time
import requests

gp.setmode(gp.BOARD)

url = 'https://vendingpi.herokuapp.com'

cardPin = 3
phonePin = 5

cokePrice = '20'
LaysPrice = '10'
KitKatPrice = '10'
DairyMilk = '30'


card1 = 11 
card2 = 13
card3 = 15
card4 = 19
card5 = 21

gp.setup(cardPin,gp.IN)
gp.setup(phonePin,gp.IN)
gp.setup(card1,gp.IN)
gp.setup(card2,gp.IN)
gp.setup(card3,gp.IN)
gp.setup(card4,gp.IN)
gp.setup(card5,gp.IN)

user1 = "X9JiHpsDt9OioCmBiX1VwSwiq7m2"  #Rohan
user2 = "Yet2jm7a5nOlc9c1cXYChcHl6cp1"  #Dhanush
user3 = "cpqSQeFfnMf6HrKwGIv2f0TcQB72"  #Shireesh
user4 = "ktIzXYFnnwZrqL1UQy23j226dLz2"  #Raghav
 
def updateItemCount(name):
    r = req.post(url + '/api' + '/update' + '/item/' + name)
    d = r.text
    print(d)

def updateWalletBalance(userId,price):
    r = req.post(url + '/api' + '/update/' + 'wallet/' + userId + '/'+ price)
    d = r.text
    print (data)

while True:
    if   gp.input(cardPin) == 1:
        print('Card Mode')
        if gp.input(card1) == 1:
            print('Rohan')
            


    elif gp.input(phonePin) == 1:
    

    else:
        print('NO Mode')



