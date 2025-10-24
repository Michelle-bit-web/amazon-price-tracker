import requests
from bs4 import BeautifulSoup

#Fetch raw HTML content
url = "https://appbrewery.github.io/instant_pot/"

response = requests.get(url)

#Parse using BeautifulSoup
bs = BeautifulSoup(response.content, 'html.parser')
# print(bs.prettify())
price = bs.find('span', class_='aok-offscreen').get_text()

#Remove $ Sign
price_number = price.split('$')[1]
# print(price_number)

#Convert to floating point number
price_as_float = float(price_number)
print(price_as_float)