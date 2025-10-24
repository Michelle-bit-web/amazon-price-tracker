<div>
  <img src="./images/logo_price_tracker.png" alt="Amazon Price Tracker Logo" width="120">
</div>

# Amazon Price Tracker 

A simple Python script that automatically tracks the price of an Amazon product and sends an email alert when the price drops below your desired threshold.
It uses BeautifulSoup to scrape product data and smtplib to send email notifications securely via SMTP.

### 📦 Features

- Fetches live price and product title from any Amazon product page.
- Sends an automatic email alert when the price drops below a target value.
- Uses environment variables to keep credentials secure.
- Can be easily customized for any product URL.

### ⚙️ Requirements

- Python 3.8+

- The following libraries: `pip install requests beautifulsoup4 python-dotenv`

### 🧰 Setup Instructions
1. Clone or download this repository
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker

2. Create a .env file

In the project root, create a file named .env and add your credentials:

- SMTP_ADDRESS=smtp.gmail.com
- EMAIL_ADDRESS=your_email@example.com
- EMAIL_PASSWORD=your_email_password


💡 Use an App Password if you’re using Gmail with 2-Factor Authentication.

3. Update the product URL

Inside the script, replace the existing live_url with your own product link:

live_url = "https://www.amazon.de/your-product-link"

4. Set your target price

Modify the BUY_PRICE variable in the script:

BUY_PRICE = 155

🚀 Run the Script

Execute the script with:

`python main.py`


If the product’s price is lower than your defined BUY_PRICE,
you’ll receive an email notification with the product title and link.

### 🧠 How It Works

- Requests fetches the raw HTML of the Amazon product page.
- BeautifulSoup parses and extracts the current price and title.
- The price is converted to a float for comparison.
- If the price is below the target threshold, smtp library sends an email alert.

### 🛡️ Notes

Amazon’s page structure may change over time, which can break the scraper.
If that happens, inspect the product page and update the HTML element selectors.

You can run the script periodically (e.g., via cron job or Task Scheduler) to automate price tracking.

### 🖋️ License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it.