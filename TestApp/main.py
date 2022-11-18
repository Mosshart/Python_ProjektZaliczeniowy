# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests

def checkIsPrime(param):
    url = ""
    status = requests.get(url, param)
    print('liczba jest: ' + status)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    checkIsPrime(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
