import RPi.GPIO as gp
import time
import requests as req

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
cardSuccess = 19
Mode = 21

gp.setup(cardPin, gp.IN)
gp.setup(phonePin, gp.IN)
gp.setup(card1, gp.IN)
gp.setup(card2, gp.IN)
gp.setup(card3, gp.IN)
gp.setup(cardSuccess, gp.IN)
gp.setup(Mode, gp.OUT)

user1 = "X9JiHpsDt9OioCmBiX1VwSwiq7m2"  # Rohan
user2 = "Yet2jm7a5nOlc9c1cXYChcHl6cp1"  # Dhanush
user3 = "cpqSQeFfnMf6HrKwGIv2f0TcQB72"  # Shireesh
user4 = "ktIzXYFnnwZrqL1UQy23j226dLz2"  # Raghav

priceArray = [cokePrice, LaysPrice, KitKatPrice, DairyMilk]


def getMode():
    r = req.get(url + '/api' + '/get' + '/mode')
    k = r.json()
    return k


def updateItemCount(name):
    r = req.post(url + '/api' + '/update' + '/item/' + name)
    d = r.text
    print(d)


def updateWalletBalance(userId, price):
    r = req.post(url + '/api' + '/update/' + 'wallet/' + userId + '/' + price)
    d = r.text
    print(d)


if __name__ == '__main__':
    while True:
        f = getMode()
        mode = f['mode']
        user = f['user']
        selected = f['selected']
        if mode == 'Card':
            gp.output(Mode, 1)
            if gp.input(cardSuccess) == 1:
                f = updateWalletBalance(user, priceArray[int(selected) - 1])
                if f == 'OK':
                    gp.output(Mode, 0)
                    break
        else:
            print('Coin Mode')
