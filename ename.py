import requests
from bs4 import BeautifulSoup

'''
@author: github/wolverinn
@date: 04/27/2018

requirements:
    Python 3.x
    requests
    bs4

function: 根据中文名和性别，起一个地道英文名，调用了扇贝网的接口
'''

url1="http://ename.shanbay.com.cn/?gender="
url2="&name_cn="
url3="&for_friend=0"

n=input("input your chinese name:")
g=input("input your gender(m for male/f for female)")
if g=="m":g="1"
if g=="f":g="0"
def get_name(n):
    url=url1+g+url2+n+url3
    nameweb = requests.get(url)
    soup = BeautifulSoup(nameweb.text, 'html.parser')
    name1 = soup.find('div', attrs={'class': 'name-container'})
    name = name1.find('span', attrs={'class': 'name-en'})
    print(name.string)

i=1
while i==1:
    get_name(n)
    con=input("continue?y/n")
    if con=="y" or con=="":
        i=1
    else:
        i=0
