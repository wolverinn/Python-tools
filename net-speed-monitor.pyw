import os
import re
import time
import getpass
from tkinter import *

'''
@author: github/wolverinn
@date: 07/29/2018

requirements: only Python 3

function:实时显示计算机上传和下载速度
'''

def start():
    while(True):
        #取一次数据开始计时
        count_start=time.time()
        raw_info = os.popen("netstat -e")
        temp = raw_info.readlines()
        info_str = temp[4]
        info = re.findall('\d+', info_str)
        upload_before = int(info[1])
        download_before = int(info[0])
        time.sleep(0.8)
        count_end=time.time()
        #取第二次数据结束计时
        raw_info = os.popen("netstat -e")
        temp = raw_info.readlines()
        info_str = temp[4]
        info = re.findall('\d+', info_str)
        upload_after = int(info[1])
        download_after = int(info[0])
        time_cost=count_end-count_start
        upload_speed=(upload_after-upload_before)/time_cost/1000
        download_speed=(download_after-download_before)/time_cost/1000
        str_upload_speed=str(upload_speed)
        str_download_speed=str(download_speed)
        if 100<upload_speed<1000:
            up_display_info="U:"+str_upload_speed[:5] +"kb/s"
        else:
            up_display_info = "U:"+str_upload_speed[:4] + "kb/s"
        if 100<download_speed<1000:
            down_display_info = "D:"+str_download_speed[:5] + "kb/s"
        else:
            down_display_info = "D:"+str_download_speed[:4] + "kb/s"
        up_info["text"] = up_display_info
        down_info["text"] = down_display_info
        root.update()

#设置右键菜单
def popmenu(event):
    menu.post(event.x_root, event.y_root)
#设置调整位置的函数
def position_adjust():
    # 设置上下左右调整
    def ad_up():
        global position_xy
        if position_xy[1] > 1:
            position_xy[1] = position_xy[1] - 1
        else:
            pass
        geo = "+" + str(position_xy[0]) + "+" + str(position_xy[1])
        root.geometry(geo)
        root.update()
        posi_x.delete(0, len(posi_x.get()))
        posi_y.delete(0, len(posi_y.get()))
        posi_x.insert(END, str(position_xy[1]))
        posi_y.insert(END, str(position_xy[0]))
        ad_window.update()
    def ad_down():
        global position_xy
        position_xy[1] = position_xy[1] + 1
        geo = "+" + str(position_xy[0]) + "+" + str(position_xy[1])
        root.geometry(geo)
        root.update()
        posi_x.delete(0, len(posi_x.get()))
        posi_y.delete(0, len(posi_y.get()))
        posi_x.insert(END, str(position_xy[1]))
        posi_y.insert(END, str(position_xy[0]))
        ad_window.update()
    def ad_left():
        global position_xy
        position_xy[0] = position_xy[0] - 1
        geo = "+" + str(position_xy[0]) + "+" + str(position_xy[1])
        root.geometry(geo)
        root.update()
        posi_x.delete(0, len(posi_x.get()))
        posi_y.delete(0, len(posi_y.get()))
        posi_x.insert(END, str(position_xy[1]))
        posi_y.insert(END, str(position_xy[0]))
        ad_window.update()
    def ad_right():
        global position_xy
        position_xy[0] = position_xy[0] + 1
        geo = "+" + str(position_xy[0]) + "+" + str(position_xy[1])
        root.geometry(geo)
        root.update()
        posi_x.delete(0,len(posi_x.get()))
        posi_y.delete(0, len(posi_y.get()))
        posi_x.insert(END, str(position_xy[1]))
        posi_y.insert(END, str(position_xy[0]))
        ad_window.update()
    def mannual_adjust():
        global position_xy
        position_xy[1]=posi_x.get()
        position_xy[0]=posi_y.get()
        geo = "+" + str(position_xy[0]) + "+" + str(position_xy[1])
        root.geometry(geo)
        root.update()
    def save():
        global position_xy
        user=getpass.getuser()
        save_info_path="C:/users/"+str(user)+"/AppData/Roaming/net-speed-monitor-position"
        f=open(save_info_path,'w')
        f.write(str(position_xy[0]))
        f.write(',')
        f.write(str(position_xy[1]))
        f.close()
        ad_window.destroy()
        start()
    ad_window=Tk()
    ad_window.wm_title("Adjust Position")
    ad_window.geometry("420x360")
    label_x=Label(ad_window,text="x:")
    posi_x=Entry(ad_window)
    posi_x.insert(END, str(position_xy[1]))
    label_y=Label(ad_window,text="y:")
    posi_y=Entry(ad_window)
    posi_y.insert(END,str(position_xy[0]))
    ad_button=Button(ad_window,text="Adjust Position",command=mannual_adjust)
    line1=Label(ad_window,text="----------------------------------------")
    up_button=Button(ad_window,text="Up",command=ad_up)
    down_button=Button(ad_window,text="Down",command=ad_down)
    left_button=Button(ad_window,text="Left",command=ad_left)
    right_button=Button(ad_window,text="Right",command=ad_right)
    line2 = Label(ad_window, text="----------------------------------------")
    save_arg=Button(ad_window,text="Save setting",command=save)
    label_x.pack()
    posi_x.pack()
    label_y.pack()
    posi_y.pack()
    ad_button.pack()
    line1.pack()
    up_button.pack()
    down_button.pack()
    left_button.pack()
    right_button.pack()
    line2.pack()
    save_arg.pack()
    ad_window.mainloop()

#设置调整透明度的函数
def adjust_transparency():
    def adjust_trans_bn():
        global intransparency
        user=getpass.getuser()
        save_path2="C:/users/"+str(user)+"/AppData/Roaming/net-speed-monitor-tranparency"
        trans_num=ad_trans.get()
        intransparency=trans_num
        root.attributes("-alpha", trans_num)
        root.update()
        f=open(save_path2,'w')
        f.write(str(trans_num))
        f.close()
        trans.destroy()
        start()
    global intransparency
    trans=Tk()
    trans.geometry("300x200")
    trans.wm_title("Transparency")
    parency=Label(trans,text="不透明度：")
    ad_trans=Entry(trans)
    ad_trans.insert(END,intransparency)
    ad_button=Button(trans,text="确定",command=adjust_trans_bn)
    parency.pack()
    ad_trans.pack()
    ad_button.pack()
    trans.mainloop()
#设置退出程序的函数
def exit_netmonitor():
    root.destroy()
#双击开始monitor
def double_click_start(event):
    start()
#打印欢迎界面，因为打包之后必须出现命令行的无奈选择
# print('''
#         *        *    * * * * *    * * * * * *            *         *        *          *        *
#         *  *     *    *                 *                 * *     * *     *      *      *  *     *
#         *    *   *    * * * * *         *       --------  *   *  *  *    *         *    *    *   *
#         *      * *    *                 *                 *    **   *     *     *       *      * *
#         *        *    * * * * *         *                 *         *        *          *        *
#
#         -------------------------You have entered the world of net-speed-monitor----------------------
#         ---------------------------------Please keep the window open----------------------------------
#         -----------------------------------------Enjoy it!--------------------------------------------
# ''')

#初始化窗口
root = Tk()
root.wm_attributes('-topmost',1)#始终置顶
root.overrideredirect(True)
user=getpass.getuser()
file_path1="C:/users/"+str(user)+"/AppData/Roaming/net-speed-monitor-position"
file_path2="C:/users/"+str(user)+"/AppData/Roaming/net-speed-monitor-tranparency"
if os.path.exists(file_path1):
    f=open(file_path1,'r')
    position_xy=f.readline()
    position_xy=position_xy.split(",")
    f.close()
else:
    position_xy = [970, 631]
if os.path.exists(file_path2):
    f=open(file_path2,'r')
    intransparency=f.readline()
    f.close()
else:
    intransparency=0.8
try:
    position_xy[0]=int(position_xy[0])
    position_xy[1]=int(position_xy[1])
    intransparency=float(intransparency)
except:
    position_xy = [970, 631]
    intransparency=0.8
root.attributes("-alpha", intransparency)#窗口不透明度
geo="+"+str(position_xy[0])+"+"+str(position_xy[1])
root.geometry(geo)#设置窗口大小和位置
menu=Menu(root)#设置右键菜单：退出程序以及调整方向
menu.add_command(label="Start monitoring",command=start)
menu.add_command(label="Adjust tranparency",command=adjust_transparency)
menu.add_command(label="Adjust position",command=position_adjust)
menu.add_command(label="Exit",command=exit_netmonitor)
root.bind("<Button-3>",popmenu)
root.bind("<Double-Button-1>",double_click_start)
up_info = Label(root,fg="red", text="U:--kb/s")
down_info = Label(root,fg="green", text="D:--kb/s")
up_info.after(600,start)#600ms后开始刷新窗口获取数据
up_info.pack()
down_info.pack()
root.mainloop()
