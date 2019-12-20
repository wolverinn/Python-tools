'''
    知乎视频下载器，只需手动添加要下载的视频id（在视频链接的末尾）
    视频链接：收藏之后在收藏夹中点开回答便可找到视频链接
    可选：添加多个视频id，选择视频质量,ld/hd/sd分别为标清/高清/超清
'''

import requests
import subprocess
from tkinter import *

'''
@author: github/wolverinn
@date: 07/27/2018

requirements:
- Python 3.x
- requests
- ffmpeg (add to PATH)

待改进：直接下载回答下面的所有视频
下载时应该创建线程以防止窗口停止响应
'''

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36",
    "Content-Type": "application/json",
    "Origin": "https://v.vzuu.com"
}
def download_m3u8_url(QUALITY,video_id):
    headers["Referer"]="https://v.vzuu.com/video/"+str(video_id)
    headers["X-Referer"]="https://link.zhihu.com/?target=https%3A//www.zhihu.com/video/"+str(video_id)
    ses=requests.session()
    ses.get("https://www.zhihu.com/collection/253903004")
    info_url="https://lens.zhihu.com/api/videos/"+str(video_id)
    video_info=ses.get(info_url,headers=headers)
    # print(video_info.text)
    m3u8_url=video_info.json()["playlist"][QUALITY]["play_url"]
    # print(m3u8_url)
    sub_cmd="ffmpeg -i "+str(m3u8_url)+" -c copy "+str(video_id)+".mp4"
    subprocess.call(sub_cmd)

def click():
    if v.get()==2:
        QUALITY="hd"
    elif v.get()==3:
        QUALITY="sd"
    else:
        QUALITY="ld"
    all_ids=e1.get()
    e1.delete(0, len(all_ids))
    id_list=all_ids.split(";")
    try:
        if id_list[-1] == '':
            for video_id in id_list[0, -1]:
                download_m3u8_url(QUALITY, video_id)
        else:
            for video_id in id_list:
                download_m3u8_url(QUALITY, video_id)
    except:
        c["text"]="视频id有误，重新输入"

root=Tk()
root.geometry("360x240")
# root.iconbitmap("file_cloud.ico")
root.wm_title("知乎视频下载器")
wl=Label(root,text="输入视频id(多个id以英文分号间隔)",font="楷书 15")
e1=Entry(root,font="28")
v=IntVar()
r1=Radiobutton(root,text="标清",variable=v,value=1)
r2=Radiobutton(root,text="高清",variable=v,value=2)
r3=Radiobutton(root,text="超清",variable=v,value=3)
b1=Button(root,text="Donwload",font="Helvetica 12 bold italic",borderwidth="4",command=click)
c=Label(root,text="")
wl.pack()
e1.pack()
c.pack()
r1.pack(anchor=W)
r2.pack(anchor=W)
r3.pack(anchor=W)
b1.pack()
root.mainloop()

# import json
# info=open("info.json",'rb')
# info_json=json.load(info)
# video_ids=info_json["video_ids"]
# QUALITY=info_json["QUALITY"]
# for video_id in video_ids:
#     download_m3u8_url(QUALITY,video_id)