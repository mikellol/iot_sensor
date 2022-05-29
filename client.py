from http import client
from random import randint
from wsgiref import headers
import json
import time

_conn = client.HTTPConnection('localhost', port=5000)

h = {'Content-type':'application/json'}
x=1
while True:
    random_number = randint(0,90)
    
    data = {
        'id':x,
        'name':'Temp sensor',
        'value': random_number
    }
    json_data = json.dumps(data)
    time.sleep(5)
    _conn.request('POST', '/devices', json_data, headers=h)
    _conn.close()
    print(data)
    if(random_number >= 15):
        print("La inclinacion es mayor a 15")
    x=x+1    