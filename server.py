"""
@author M.Velarde
@since 2022-5-10
@descrip.Ejercicio de Flask
"""
#unclusion del modulo 
from flask import Flask, request
app = Flask ('__main__')

device = {
    "code":"112233",
    "descrip":"temp.sensor",
    "value":67
}

@app.route('/test', methods=['GET'])
def go_home ():
    return device

#save an user
@app.route('/users', methods=['POST'])
def save_user():
    user = request.json
    print(user)
    return user

#save a device
@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    return device

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')