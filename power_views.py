import requests
from random_userAgents import GetUserAgent
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import re
import pickle

'''
@author: github/wolverinn
@date: 12/19/2019

requirements:
- Python 3.x
- requests
- selenium
- chrome
- chrome driver with the right version and add to ENVironment PATH
- bs4

function:
Increase the views of a webpage. For example, a blog.
But as it doesn't change the ip address. So it only increase the number of views, not the number of viewers.
'''

def get_page(url):
    chrome_options = webdriver.ChromeOptions()
    ua_argument = 'User-Agent="'+GetUserAgent()+'"'
    chrome_options.add_argument(ua_argument)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('log-level=3')
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        #driver.set_page_load_timeout(6)
        # driver.set_script_timeout(6)
        driver.get(url)
        # time.sleep(0.5)
        driver.quit()
    except:
        driver.quit()
        print("timeout")

url = input("input jianshu url: ")
count = input("input reads: ")
for i in range(int(count)):
    get_page(url)
    print("visited time: {}".format(i))