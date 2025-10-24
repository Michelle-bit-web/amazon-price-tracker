import requests
from bs4 import BeautifulSoup
import smtplib
import os

from flask.cli import load_dotenv

#Load .env file
load_dotenv()

SMTP_ADDRESS=os.getenv('SMTP_ADDRESS')
EMAIL_ADDRESS=os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD=os.getenv('EMAIL_PASSWORD')

#Fetch raw HTML content
url = "https://appbrewery.github.io/instant_pot/"
live_url = "https://www.amazon.de/gp/aw/d/B0854FJNSD/?_encoding=UTF8&pd_rd_plhdr=t&aaxitk=8a39a5691104864212aadbc708255a6f&hsa_cr_id=0&qid=1761306899&sr=1-1-e0fa1fdd-d857-4087-adda-5bd576b25987&aref=Gcq4NQYxli&ref_=sbx_s_sparkle_sbtcd_asin_0_img&pd_rd_w=cxeC8&content-id=amzn1.sym.17ff4c80-d3f6-4458-af23-4ad6a620d092%3Aamzn1.sym.17ff4c80-d3f6-4458-af23-4ad6a620d092&pf_rd_p=17ff4c80-d3f6-4458-af23-4ad6a620d092&pf_rd_r=PVA8EVER0804HF5HG9A7&pd_rd_wg=xdE3k&pd_rd_r=74e88109-0f09-4ccd-9deb-f278f2c3ea22&th=1"

headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(live_url, headers=headers)

#Parse using BeautifulSoup
bs = BeautifulSoup(response.content, 'html.parser')
# print(bs.prettify())
price = bs.find('span', class_='aok-offscreen').get_text()
# print(price)

#Remove € Sign
price_number = price.split('€')[0]
# print(price_number)

#Convert to floating point number
price_as_float = float(price_number.replace(",", "."))
print(price_as_float)

# ==== Send an Email ====
#Get product title
title = bs.find(id="productTitle").get_text().strip()
# print(title)

#Desired maximum price
BUY_PRICE = 155

if price_as_float < BUY_PRICE:
    message = f"{title} is on sale for {price_number}"
    print(message)
    with smtplib.SMTP(SMTP_ADDRESS, port=587) as connection:
        connection.starttls()
        result = connection.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_ADDRESS,
            to_addrs=EMAIL_ADDRESS,
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )