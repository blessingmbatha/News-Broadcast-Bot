import os
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
import locale

driver_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
locale.setlocale(locale.LC_TIME, "ja_JP.UTF-8")

def news_scraper():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.get(url='https://news.yahoo.co.jp/categories/it')
    html_source = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html_source, "html.parser")
    content_divs = soup.find_all('li', class_='newsFeed_item')
    # print(content_divs[0])
    for div in content_divs:
        date_tag = div.find('time', class_='newsFeed_item_date')
        if date_tag != None:
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = date.strftime("%Y")
            date_text = year + "/" + date_tag.text
            date_obj   = datetime.datetime.strptime(date_text, '%Y/%m/%d(%a) %H:%M')
            # print(date_obj.date())
            if date_obj.date() != datetime.datetime.now().date():
                continue
            print(date_obj.date())
    # print(locale.getlocale(locale.LC_TIME))

news_scraper()