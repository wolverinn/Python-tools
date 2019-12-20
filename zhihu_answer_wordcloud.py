import html2text
import requests
import re
import jieba
from wordcloud import WordCloud
import os
# sudo apt-get install python3-tk

'''
@author: github/wolverinn
@date: 01/20/2019

requirements:
    Python 3.x
    requests
    html2text
    jieba
    wordcloud

function:
Input a zhihu question URL, get 150 answers, save them to markdown, and generates wordcloud.

待添加功能：输入答案URL，保存答案到markdown
'''

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
    "Host": "www.zhihu.com",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
question = []

def get_flow():
    h = html2text.HTML2Text()
    h.ignore_links = True
    h.ignore_images = True
    h.ignore_emphasis = True
    h.ignore_tables = True
    filename = "{}.txt".format(question_id)
    f = open(filename,'w',encoding='utf-8')
    for i in range(15):
        limit = "10"
        offset = str(i*10)
        print("getting the {} answer...".format(offset))
        api_base_url = "https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B%2A%5D.is_normal%2Ccontent%2Ceditable_content%2Cvoteup_count&limit={}&offset={}&platform=desktop&sort_by=default".format(question_id,limit,offset)
        answer_flow = requests.get(api_base_url,headers=headers)
        if answer_flow.status_code == 200:
            answer_data = answer_flow.json()["data"]
            question.append(answer_data[0]["question"]["title"])
            answer_count = answer_flow.json()["paging"]["totals"]
            if int(answer_count) < int(offset) + 10:
                return 0
            for single_answer in answer_data:
                single_content = single_answer["content"]
                single_vote = single_answer["voteup_count"]
                converted_content = h.handle(single_content)
                f.write(converted_content)
                f.write('\n')
    f.close()

def seg_answer():
    answer_content = open(question_id + ".txt",'r',encoding='utf-8').read()
    print("segging answers...")
    answer_seg = jieba.cut(answer_content)
    stopwords = open("chineseStopWords.txt",'r',encoding='GBK').read()
    new_answer_seg = []
    for text in answer_seg:
        if text not in stopwords:
            new_answer_seg.append(text)
    string = ' '.join(new_answer_seg)
    print("making wordcloud...")
    wc = WordCloud(font_path='C:/Windows/Fonts/arial.ttf',background_color='white',width=1000,height=800).generate(string)
    wc.to_file(question[0]+'.png')

question_url = input("输入知乎问题链接（如：https://www.zhihu.com/question/23819007）：")
valid_check = re.search('question/\d*',question_url)
if valid_check:
    question_id = valid_check.group().replace("question/",'')
    get_flow()
    print("required answers saved successfully")
    seg_answer()
    img_name = ".\\"+"\""+question[0]+".png"+"\""
    os.system(img_name)
    # print(question_id)
else:
    print("Not a valid zhihu question URL !")
