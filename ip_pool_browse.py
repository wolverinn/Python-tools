import sqlite3
from selenium import webdriver
from random_userAgents import GetUserAgent
import re
# import time

'''
@author: github/wolverinn
@date: 01/31/2019

requirements:
    Python 3.x
    random_userAgents.py
    free-ip-pool.py: to create and add ip to ip pool

function:
Use the proxies in the ip pool to browse the web pages. To increase the viewers of the web page.
'''

conn = sqlite3.connect('pool.db')
c = conn.cursor()
ip_list = list(c.execute("SELECT * FROM IP"))
print("existing proxies in table IP:{}".format(str(len(ip_list))))

def auto_open(url,ip_port):
    chrome_options = webdriver.ChromeOptions()
    usr_agents = GetUserAgent()
    proxy_argument = "--proxy-server=http://" + ip_port
    ua_argument = 'User-Agent="'+usr_agents+'"'
    chrome_options.add_argument(proxy_argument)
    chrome_options.add_argument(ua_argument)
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('log-level=3')
    try:
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver.set_page_load_timeout(6)
        # driver.set_script_timeout(6)
        driver.get(url)
        # time.sleep(0.5)
        a = driver.page_source
        if re.search("ERR_PROXY_CONNECTION_FAILED",a):
            print("connection error:{}".format(ip_port))
            driver.quit()
            return False
        else:
            print("200 OK")
            driver.quit()
            return True
    except:
        # time.sleep(3)
        driver.quit()
        print("timeout:{}".format(ip_port))
        return False

url = input("input the url:")
valid_sum = 0
for i,ip_port in enumerate(ip_list):
    if i>0 and i%50 is 0:
        print("used {} ip".format(str(i)))
        print("ip valid:{}".format(str(valid_sum)))
    result = auto_open(url,ip_port[1])
    if result:
        valid_sum = valid_sum + 1
    else:
        del_cmd = "DELETE FROM IP WHERE IPPORT = \"" + ip_port[1] + "\""
        c.execute(del_cmd)
        conn.commit()

conn.close()