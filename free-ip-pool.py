import requests
import os
import webbrowser
from bs4 import BeautifulSoup
import sqlite3
import json
import time
import random
from selenium import webdriver
import re

'''
@author: github/wolverinn
@date: 02/01/2019

requirements:
    Python 3.x
    requests
    bs4
    selenium
    chrome
    chrome driver(add to PATH)

function:
Crawls free proxies from several websites that offer them, and save them to a database to build an ip pool.
Also validates the ip in the pool.

待改进：使用多线程验证IP有效性
'''

conn = sqlite3.connect('pool.db')
c = conn.cursor()
try:
    c.execute('''CREATE TABLE IP
        (ID INTEGER PRIMARY KEY AUTOINCREMENT,
        IPPORT VARCHAR(50) NOT NULL UNIQUE);''')
    conn.commit()
    print("created new table IP")
except:
    pass
print("existing proxies in table IP:{}".format(str(len(list(c.execute("SELECT * FROM IP"))))))

def GetUserAgent():
    '''
    功能：随机获取HTTP_User_Agent
    '''
    user_agents=[
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
    ]
    user_agent = random.choice(user_agents)
    return user_agent

def get_xici():
    print("getting ip from xicidaili.com...")
    headers_xici = {
        "Host": "www.xicidaili.com",
        "Referer": "https://www.xicidaili.com/nn/1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    # webbrowser.open("https://www.xicidaili.com/nn/1")
    # cookie = input("input a valid cookie for xicidaili.com first:")
    # headers_xici[""]
    # 只爬取xici前3页的IP，后面的验证时间太久了失效的可能性大,ps:这个网站会封IP...
    for i in range(3):
        ses = requests.session()
        ses.get("https://www.xicidaili.com/nn/1")
        xici_url = "https://www.xicidaili.com/nn/{}".format(str(i+1))
        xici_req = requests.get(xici_url,headers=headers_xici)
        print(xici_req.status_code)
        if xici_req.status_code == 200:
            soup = BeautifulSoup(xici_req.text,'html.parser')
            ip_table = soup.find('table',attrs={'id':'ip_list'})
            trs = ip_table.find_all('tr')
            for i,tr in enumerate(trs):
                if i>0:
                    td = tr.find_all('td')
                    ip_port = td[1].string + ":" + td[2].string
                    print(ip_port)
                    insert_cmd = "INSERT INTO IP (IPPORT) VALUES ('{}')".format(ip_port)
                    try:
                        c.execute(insert_cmd)
                        conn.commit()
                    except:
                        pass
                    # temp_set.add(ip_port)
        time.sleep(2)

def get_66ip():
    print("getting ip from 66ip.cn...")
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "en-US,en;q=0.9",
        "Cache-Control": "max-age=0",
        "Connection": "keep-alive",
        #"Cookie": "yd_cookie=14383921-5354-46e8e6700ba090ad2c96a202cbb6d2145786; _ydclearance=3b1c64af06ff7ca0605ca864-eaf1-4a18-bbb8-b239a592ed41-1547569877",
        "DNT": "1",
        "Host": "www.66ip.cn",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    }
    webbrowser.open("http://www.66ip.cn/areaindex_1/1.html")
    cookie = input("input a valid cookie for 66ip.cn first:")
    headers["Cookie"] = cookie
    ses = requests.session()
    for i in range(26):
        fucking_url = "http://www.66ip.cn/areaindex_{}/1.html".format(str(i+1))     #每个地区只有第一页的是最近验证的
        addr = ses.get(fucking_url,headers=headers)
        print("getting the {} page of 66ip.cn...".format(str(i)))
        if addr.status_code == 200:
            soup = BeautifulSoup(addr.content,'html.parser')
            table = soup.find_all('table')[2]
            trs = table.find_all('tr')
            for i,tr in enumerate(trs):
                if i > 0:
                    td = tr.find_all('td')
                    ip_port = td[0].string+ ":" + td[1].string
                    # print(ip_port)
                    # temp_set.add(ip_port)
                    try:
                        insert_cmd = "INSERT INTO IP (IPPORT) VALUES ('{}')".format(ip_port)
                        c.execute(insert_cmd)
                        conn.commit()
                    except:
                        pass
        time.sleep(0.5)

def get_freeproxylist():
    print("getting ip from freeproxylist...")
    fpl_url = "http://proxylist.fatezero.org/proxy.list"
    proxy_list = requests.get(fpl_url)
    if proxy_list.status_code == 200:
        lines = proxy_list.text.split('\n')
        for i,line in enumerate(lines):
            try:
                content = json.loads(line)
            except:
                continue
            if str(content["anonymity"]) == "high_anonymous" and str(content["type"]) == "http" and str(content["country"]) == "CN":
                ip_port = str(content["host"]) + ":" + str(content["port"])
                # print(ip_port)
                # temp_set.add(ip_port)
                insert_cmd = "INSERT INTO IP (IPPORT) VALUES ('{}')".format(ip_port)
                c.execute(insert_cmd)
                conn.commit()
            if i%1000 == 0:
                print("processed {} in free proxy list".format(str(i)))

def add_ip():
    get_freeproxylist()
    get_xici()
    get_66ip()
    print("total ip count:{}".format(str(len(list(c.execute("SELECT * FROM IP"))))))

def test_ip():
    ip_list = list(c.execute("SELECT * FROM IP"))
    test_url = "http://www.baidu.com/"
    for i,ip_port in enumerate(ip_list):
        if i>0 and i%100 is 0:
            print("testing {} ip".format(str(i)))
        user_agent = GetUserAgent()
        header = {
            "User-Agent":user_agent,
        }
        proxy = {
            'http': ip_port[1],
            # 'https': 'https://' + proxy,
        }
        try:
            r = requests.get(test_url,headers=header,proxies=proxy,timeout=5)
            print(r.status_code)
        except:
            del_cmd = "DELETE FROM IP WHERE IPPORT = \"" + ip_port[1] + "\""
            c.execute(del_cmd)
            conn.commit()
            print("failed:{}".format(ip_port[1]))
    print("total ip count:{}".format(str(len(list(c.execute("SELECT * FROM IP"))))))

while(1):
    print("1) add more ip to ip pool")
    print("2) test avaliability of ip in the ip pool")
    print("3) exit")
    user_choice = input("\ninput your choice: ")
    if user_choice == "1":
        add_ip()
    elif user_choice == "2":
        test_ip()
    elif user_choice == "3":
        break
    else:
        continue
conn.close()
