import requests as req

url = 'https://vendingpi.herokuapp.com'

def getJson():
    r = req.get(url + '/' + 'api' + '/getjson')
    k = r.json()
    return k

def updateItemCount(name):
    r = req.post(url + '/api' + '/update' + '/item/' + name)
    d = r.text
    print(d)


if __name__ == '__main__':
    # print(getJson())
    updateItemCount('Coke')