from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import re
import time


PATH = "C://Program Files (x86)//chromedriver.exe"
driver = webdriver.Chrome(PATH)

url = 'https://www.theweathernetwork.com/ca/hourly-weather-forecast/ontario/toronto'
driver.maximize_window()
driver.get(url)

time.sleep(5)
content = driver.page_source.encode('utf-8').strip()
soup = BeautifulSoup(content, 'lxml')
for match in soup.find_all('div', class_='wx-summary'):
    print(match.text)

driver.quit()
