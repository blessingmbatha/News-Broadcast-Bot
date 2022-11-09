import os
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time, datetime
import locale
from linebot.models import TemplateSendMessage, CarouselTemplate, CarouselColumn, URIAction
from app import line_bot_api

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

    news_list = []

    # print(content_divs[0])
    for div in content_divs:
        date_tag = div.find('time', class_='newsFeed_item_date')
        title_tag = div.find('div', class_='newsFeed_item_title')
        img_tag = div.find('img', class_='Thumbnail__ThumbnailImage-jpEmUQ fNlNnw')
        link_tag = div.find('a', class_='newsFeed_item_link')
        if date_tag != None:
            ### date data
            currentDateTime = datetime.datetime.now()
            date = currentDateTime.date()
            year = date.strftime("%Y")
            date_text = year + "/" + date_tag.text
            date_obj   = datetime.datetime.strptime(date_text, '%Y/%m/%d(%a) %H:%M')
            ### title data
            title_obj = title_tag.text
            ### img data
            img_obj = img_tag.attrs.get('src')
            ### link data
            link_obj = link_tag.attrs.get('href')
            # print(date_obj.date())
            if date_obj.date() != datetime.datetime.now().date():
                continue

            news = {
                'title' : title_obj,
                'date' : date_obj,
                'url' : link_obj,
                'img_url' : img_obj
            }
            news_list.append(news)
    carousel_columns = []

    for news in news_list :
        carousel_column = CarouselColumn(
            thumbnail_image_url=news.get('img_url'),
            title=news.get('title'),
        )
        print(news.get('title'))
        print(news.get('date'))
        print(news.get('url'))
        print(news.get('img_url'))

    # print(locale.getlocale(locale.LC_TIME))

news_scraper()