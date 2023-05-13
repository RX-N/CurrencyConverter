import requests

key = '40H98M3QLBHI1OUH'

frm = input("Enter currency to convert from: ")
to = input("Enter currency to convert to: ")

fnc = 'CURRENCY_EXCHANGE_RATE'
base_url = 'https://www.alphavantage.co/query'
url = f'{base_url}?function={fnc}&from_currency={frm}&to_currency={to}&apikey={key}'

r = requests.get(url)
data = r.json()

print(data)
