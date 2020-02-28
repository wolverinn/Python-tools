import html2text
import requests
import re
import os

'''
@author: github/wolverinn
@date: 12/19/2019

requirements:
- Python 3.x
- html2text
- requests

function:
A simple implementation using html2text library. Save the webpage to markdown.
Useful when the webpage is an article.

当然，还存在很多可以改进的地方，有时图片没法保存下来
最重要的是大部分情况下会保存除了文章之外的杂乱信息影响排版
TODO: Sometimes can't save pictures
Save only the article, trim other content
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
}

def get_flow(page_url):
    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = False
    h.ignore_emphasis = False
    h.ignore_tables = False
    filename = "{}.txt".format(page_url.split('/')[-1])
    f = open(filename,'w',encoding='utf-8')
    r = requests.get(page_url,headers=headers)
    if r.status_code == 200:
        converted_content = h.handle(r.text)
        f.write(converted_content)
        f.write('\n')
    f.close()

page_url = input("输入链接：")
get_flow(page_url)
print("required page saved successfully")
