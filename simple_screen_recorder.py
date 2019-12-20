from tkinter import *
import os
import getpass
import time
import subprocess
import win32con
import ctypes
import ctypes.wintypes
import threading

'''
@author: github/wolverinn
@date: 08/09/2018

requirements:
- Python 3.x
- pywin32
- ffmpeg(add to PATH)

function:
Records the screen using ffmpeg.
Supports self-define frame rate, resolutions, and save location.
A 3-second delay before starting recording.
Press F10 to stop.
Remembers the settings.

待改进：选择路径时可以使用按钮来选择文件夹。参考：hide_file.py
'''

#添加ffmpeg环境变量
# try:
#     ffpath=os.getcwd()
#     set_cmd="set PATH= "+str(ffpath)+"\\ffmpeg"+";"
#     os.system(set_cmd)
# except:
#     exit(1)
# 创建键盘监听以便按下F10的时候停止录制
EXIT = False # 用来传递退出的参数
user32 = ctypes.windll.user32  # 加载user32.dll
id2=106 # 注册热键的唯一id，用来区分热键
class Hotkey(threading.Thread):

    def run(self):
        global EXIT  # 定义全局变量，这个可以在不同线程间共用。

        if not user32.RegisterHotKey(None, id2, 0, win32con.VK_F10):   # 注册快捷键F10并判断是否成功，该热键用于结束程序，且最好这么结束，否则影响下一次注册热键。
            print("Unable to register id", id2)

        # 以下为检测热键是否被按下，并在最后释放快捷键
        try:
            msg = ctypes.wintypes.MSG()
            while True:
                if user32.GetMessageA(ctypes.byref(msg), None, 0, 0) != 0:
                    if msg.message == win32con.WM_HOTKEY:
                        if msg.wParam == id2:
                            EXIT=True
                            return
                    user32.TranslateMessage(ctypes.byref(msg))
                    user32.DispatchMessageA(ctypes.byref(msg))
        finally:
            user32.UnregisterHotKey(None, id2)# 必须得释放热键，否则下次就会注册失败，所以当程序异常退出，没有释放热键，
                                              # 那么下次很可能就没办法注册成功了，这时可以换一个热键测试

def control(a):
    # 监听按键
    hotkey=Hotkey()
    hotkey.run()
    while(True):
        if EXIT == True:
            global self_destroy
            self_destroy=True
            endcmd = "q".encode('utf-8')
            a.stdin.write(endcmd)
            a.communicate()
            print("Recording info:")
            size=str(os.path.getsize(video_name)/1000)+"kb"
            print("Resolution:",resolution,"\t帧数:",quality,"\tSize:",size)
            print("Recording saved to:",video_loc)
            os.system("pause")

def start():
    global quality
    global video_loc
    global resolution
    global filepath,video_name
    video_loc=loc_et.get()
    quality=e1.get()
    res_ind=v.get()-1
    resolution=["1920x1080","1280x720","720x480"][res_ind]
    # 保存设置信息
    try:
        quality=int(quality)
    except:
        quality=20
    if quality>60 or quality<0:
        print("quality more than 60")
        quality=20
    f=open(filepath,'w')
    f.write(video_loc)
    f.write(',')
    f.write(str(quality))
    f.write(',')
    f.write(resolution)
    f.close()
    try:
        save_path=video_loc.replace('\\','/')
    except:
        save_path=video_loc
    if save_path[-1] == "/":
        save_path=save_path[:-1]
    try:
        os.listdir(save_path)
    except:
        user=getpass.getuser()
        save_path = "C:/users/" + str(user) + "/desktop"
        print("invalid save path,the video will be saved to desktop")
    root.destroy()
    # 提示3秒后开始录制
    for i in range(3):
        start_win = Tk()
        start_win.overrideredirect(True)
        start_win.geometry("+400+300")
        start_win.attributes("-alpha", 0.6)
        msg = Label(start_win, text="starts in:")
        show_time=str(3-i)
        msg_time_count = Label(start_win, text=show_time, font="楷书 36")
        msg.pack()
        msg_time_count.pack()
        start_win.update()
        time.sleep(1)
        start_win.destroy()
    # 创建录制命令
    t=time.time()
    t=str(t).split('.')[0]
    video_name=save_path+"/ouput_"+t+".mkv"
    start_cmd = "ffmpeg -f gdigrab -r " + str(
        quality) + " -i desktop -vcodec libx264 -s "+resolution+" \"" + save_path + "/ouput_"+t+".mkv\""
    # libvpx-vp9
    a=subprocess.Popen(start_cmd,stdin=subprocess.PIPE)
    control(a)

self_destroy=True
while(self_destroy):
    # 读取设置信息
    self_destroy=False
    user = getpass.getuser()
    filepath = "C:/users/" + str(user) + "/AppData/Roaming/screen_capture_tool_setting"
    if os.path.exists(filepath):
        try:
            f = open(filepath, 'r')
            info = f.readline().split(',')
            video_loc = info[0]
            quality = info[1]
            resolution = info[2]
            quality = int(quality)
            f.close()
        except:
            video_loc = "C:/users/" + str(user) + "/Videos"
            quality = 20
            resolution = "720x480"
    else:
        video_loc = "C:/users/" + str(user) + "/Videos"
        quality = 20
        resolution = "720x480"
    if quality > 60 or quality < 0:
        quality = 20

    # 创建主窗口
    video_name = "ouput.mkv"
    root = Tk()
    # root.iconbitmap("camera.ico")
    root.geometry("420x270")
    root.wm_title("Simple screen recording tool")
    loc_lbl = Label(root, text="Video save location:")
    loc_et = Entry(root)
    loc_et.insert(0, video_loc)
    l1 = Label(root, text="帧数:")
    e1 = Entry(root)
    e1.insert(END, str(quality))
    loc_lbl.pack()
    loc_et.pack()
    l1.pack()
    e1.pack()
    res_lbl = Label(root, text="分辨率:")
    res_lbl.pack(anchor=W)
    v = IntVar()
    r1 = Radiobutton(root, text="1080p", variable=v, value=1)
    r2 = Radiobutton(root, text="720p", variable=v, value=2)
    r3 = Radiobutton(root, text="480p", variable=v, value=3)
    r1.pack(anchor=W)
    r2.pack(anchor=W)
    r3.pack(anchor=W)
    start_btn = Button(root, text="start", command=start)
    start_btn.pack()
    exit_lbl = Label(root, text="Press F10 to stop recording", font="宋体 20")
    exit_lbl.pack()
    root.mainloop()
