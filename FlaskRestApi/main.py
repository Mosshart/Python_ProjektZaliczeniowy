# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask
import math
from datetime import datetime
import PIL

app = Flask(__name__)

@app.route('/isPrime/<int:number>/', methods=['GET', 'POST'])
def isNumberPrime(number):
    if not isinstance(number, int): return 'Błędne dane'
    if number == 0 or number == 1:
        return 'Number is not prime'
    validationNumber = 2
    while validationNumber <= math.sqrt(number):
        if number % validationNumber < 1:
            return 'Number is not prime'
        validationNumber = validationNumber + 1
    return 'Number is prime'

@app.route('/authWithTime/<string:username>/<string:password>/', methods=['GET', 'POST'])
def returnActualTime(username, password):
    if not username == 'admin' or not password == 'admin': return 'Bledny login lub haslo'

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return "Current Time: " + current_time

@app.route('/invertImageColors/<string:imageLocalPath/', methods=['GET', 'POST'])
def invertImageColors(imageUrl):
    image = Image.open(imageUrl)
    inverted_image = PIL.ImageOps.invert(image)
    inverted_image.save('ZoltaMorda_Inverted.jpg')
#Main start
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=105)