import requests

api_key = "Enter api key"
link = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"


def get_exchange_rate(currency, currency1):
    response = requests.get(link + currency)
    data = response.json()

    if response.status_code == 200:
        rate = data["conversion_rates"][currency]
        rate1 = data["conversion_rates"][currency1]
        return rate1 / rate
    else:
        print("Failed to retrieve exchange rates")

