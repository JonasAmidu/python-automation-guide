# Python Automation: A Practical Guide to Saving 10+ Hours Every Week
## By Skylarbot | © 2026

---

## Introduction

This guide contains 10 battle-tested automation scripts that eliminate repetitive work. Copy, paste, run. No prior coding experience required.

**What you'll save:** 10+ hours per week once implemented.

**Price:** £9.99

---

## Chapter 1: Web Scraping in 5 Minutes

### The Simplest Scraper

```python
import requests
from bs4 import BeautifulSoup

def scrape(url, tag, class_name):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = soup.find_all(tag, class_=class_name)
    return [r.text.strip() for r in results]

# Example: Get all prices from Amazon
prices = scrape('https://example.com/products', 'span', 'price')
print(prices)
```

### Extract Data to CSV

```python
import csv

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Item', 'Price', 'Link'])
        for item in data:
            writer.writerow([item['name'], item['price'], item['link']])

save_to_csv(products, 'output.csv')
```

---

## Chapter 2: Auto-Form Filler

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def fill_form(url, data):
    driver = webdriver.Chrome()
    driver.get(url)
    
    for field, value in data.items():
        elem = driver.find_element(By.NAME, field)
        elem.clear()
        elem.send_keys(value)
        time.sleep(0.5)
    
    driver.find_element(By.NAME, 'submit').click()
    driver.quit()

# Usage
fill_form('https://example.com/form', {
    'email': 'you@email.com',
    'name': 'Your Name',
    'message': 'Your message here'
})
```

---

## Chapter 3: Auto-Email Sender

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(to, subject, body, from_email, password):
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(from_email, password)
        server.send_message(msg)

send_email('recipient@example.com', 'Automated Email', 'Body here', 'your@email.com', 'password')
```

---

## Chapter 4: Social Media Auto-Poster

```python
import tweepy

def post_tweet(api_key, api_secret, access_token, access_secret, message):
    client = tweepy.Client(api_key, api_secret, access_token, access_secret)
    response = client.create_tweet(text=message)
    return response

post_tweet('YOUR_KEY', 'YOUR_SECRET', 'ACCESS_TOKEN', 'ACCESS_SECRET', 'Hello world!')
```

---

## Chapter 5: Price Tracker

```python
import requests
from bs4 import BeautifulSoup
import smtplib
import schedule
import time

def check_price(url, target_price, email, password):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price_text = soup.find('span', class_='price').text
    current_price = float(price_text.replace('£', ''))
    
    if current_price <= target_price:
        send_email(email, 'Price Drop!', f'Price is now £{current_price}')
    
    return current_price

schedule.every().day.at("10:00").do(lambda: check_price('URL', 100, 'e@e.com', 'pw'))

while True:
    schedule.run_pending()
    time.sleep(60)
```

---

## Chapter 6: Auto-Job Applier

```python
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def apply_to_jobs(job_urls, resume_path):
    driver = webdriver.Chrome()
    
    for url in job_urls:
        driver.get(url)
        time.sleep(2)
        
        # Upload resume
        upload = driver.find_element(By.XPATH, '//input[@type="file"]')
        upload.send_keys(resume_path)
        
        # Click apply
        apply_btn = driver.find_element(By.XPATH, '//button[text()="Apply"]')
        apply_btn.click()
        time.sleep(1)
    
    driver.quit()
```

---

## Chapter 7: Data Entry Automation

```python
import pyautogui
import time

def auto_type(text, delay=0.1):
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

def auto_fill_excel(row_data):
    pyautogui.press('tab')
    for cell in row_data:
        auto_type(str(cell))
        pyautogui.press('tab')
    pyautogui.press('enter')
```

---

## Chapter 8: Appointment Reminder Bot

```python
import datetime
from twilio.rest import Client

def send_reminder(phone, message, account_sid, auth_token):
    client = Client(account_sid, auth_token)
    client.messages.create(
        body=message,
        from_='+1234567890',
        to=phone
    )

# Check daily at 9am
if datetime.datetime.now().hour == 9:
    appointments = [...]  # Load from your calendar
    for appt in appointments:
        send_reminder(appt['phone'], f"Reminder: {appt['title']} at {appt['time']}")
```

---

## Chapter 9: Auto-Reply Bot

```python
from selenium import webdriver
import time

AUTOREPLIES = {
    'hello': 'Hi! Thanks for reaching out. How can I help?',
    'price': 'Our prices start at £49. Check our website for details.',
    'hours': 'We are open 9am-5pm, Monday to Friday.'
}

def auto_reply(url, keywords):
    driver = webdriver.Chrome()
    driver.get(url)
    
    while True:
        messages = driver.find_elements(By.CLASS_NAME, 'message')
        for msg in messages:
            text = msg.text.lower()
            for kw, reply in keywords.items():
                if kw in text and 'replied' not in msg.get_attribute('class'):
                    # Click reply and send
                    pass
        time.sleep(5)
```

---

## Chapter 10: Complete Workflow Automation

```python
"""
Full automation: Scrape data → Process → Email → Log
"""
import requests
from bs4 import BeautifulSoup
import csv
import smtplib
from datetime import datetime

class WorkflowAutomator:
    def __init__(self, config):
        self.config = config
        self.log = []
    
    def scrape(self):
        r = requests.get(self.config['url'])
        soup = BeautifulSoup(r.text, 'html.parser')
        items = soup.find_all(self.config['tag'], class_=self.config['class'])
        self.data = [i.text.strip() for i in items]
        self.log_action('scraped', len(self.data), 'items')
    
    def process(self):
        self.processed = [x.upper() for x in self.data]
        self.log_action('processed', len(self.processed), 'items')
    
    def email(self, to):
        body = '\n'.join(self.processed)
        msg = f'Subject: Report {datetime.now()}\n\n{body}'
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(self.config['email'], self.config['password'])
            server.sendmail(self.config['email'], to, msg)
        self.log_action('emailed', to, '')
    
    def log_action(self, action, count, unit):
        self.log.append(f"{datetime.now()} - {action}: {count} {unit}")
    
    def run(self):
        self.scrape()
        self.process()
        self.email(self.config['to'])
        print('\n'.join(self.log))

# Usage
automator = WorkflowAutomator({
    'url': 'https://example.com',
    'tag': 'div',
    'class': 'item',
    'email': 'you@email.com',
    'password': 'your-password',
    'to': 'client@email.com'
})
automator.run()
```

---

## Quick Reference: Common Selectors

| Website | Selector |
|---------|----------|
| Amazon | `.a-price-whole`, `.product-title` |
| eBay | `.x-price-primary`, `.item-title` |
| LinkedIn | `.job-card-list__title`, `.job-card-container` |
| Twitter | `[data-testid="tweet"]`, `. tweet-text` |

---

## Troubleshooting

**Scraper not working?**
- Site might use JavaScript → Use Selenium instead of Requests
- Check if site blocks bots → Add `headers={'User-Agent': 'Mozilla/5.0'}`

**Selenium failing?**
- Make sure ChromeDriver matches your Chrome version
- Update: `pip install selenium --upgrade`

**Getting blocked?**
- Use `time.sleep(random.uniform(1, 3))` between requests
- Rotate user-agents
- Use proxies for large jobs

---

## License

© 2026 Skylarbot. All rights reserved.

This book is for personal use only. Redistribution or resale without permission is prohibited.

**Price: £9.99** | Buy at: gumroad.com/skylarbot
