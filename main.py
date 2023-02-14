import requests
from bs4 import BeautifulSoup

print("Currency Converter")

while True:
    print(" ")

    from_currency = input("Enter in the currency you'd like to convert to: ").upper()

    to_currency = input("Enter in the currency you'd like to conver to: ").upper()

    amount = float(input("Enter in the amount of money: "))

    response = requests.get(
        f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={from_currency}&To={to_currency}")
    yummy_soup = BeautifulSoup(response.text, 'html.parser')
    try:
        print(yummy_soup.find('p', class_="result__BigRate-sc-1bsijpp-1 iGrAod").get_text())
    except:
        print("Cannot find that currency")



