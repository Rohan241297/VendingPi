import requests as req

url = 'http://localhost:3000'

cokePrice = '20'
LaysPrice = '10'
KitKatPrice = '10'
DairyMilk = '30'

priceArray = [cokePrice, LaysPrice, KitKatPrice, DairyMilk]


def getJson():
    r = req.get(url + '/' + 'api' + '/getjson')
    k = r.json()
    return k


def updateItemCount(name):
    r = req.post(url + '/api' + '/update' + '/item/' + name)
    d = r.text
    print(d)


def getMode():
    r = req.get(url + '/api' + '/get' + '/mode')
    k = r.json()
    return k


def updateWalletBalance(userId, price):
    r = req.post(url + '/api' + '/update/' + 'wallet/' + userId + '/' + price)
    d = r.text
    print(d)


if __name__ == '__main__':
    # print(getJson())
    # updateItemCount('Coke')
    # getMode()
    while True:
        f = getMode()
        mode = f['mode']
        user = f['user']
        selected = f['selected']
        if mode == 'Card':
            updateWalletBalance(user, priceArray[int(selected)-1])
            break
        else:
            print('Coin Mode')
