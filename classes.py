import requests


class P1:
    def pay(self, amount, currency):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json',
        }

        data = f'{{"amount":{amount},"currency":{currency}}}'

        response = requests.post('http://localhost:5000/v1/charge', headers=headers, data=data)
        print(response.text)


prov = P1()
prov.pay(5, "EUR")

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
