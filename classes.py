import requests
import json


class P1:
    def pay(self, amount, currency):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = {"amount": amount, "currency": currency}

        response = requests.post('https://pythonweekend-ke.herokuapp.com/v1/charge', headers=headers, data=json.dumps(data))
        print(response.status_code)


prov = P1()

prov.pay("6", "EUR")

"""
class P2:
    def pay(self, merchant, amount, currency):


class P3:
    def pay(self, ):



class Payment :
    def __init__(self, amount, currency):
        self.currency = currency
        self.currency = amount
"""
