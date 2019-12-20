import json
import os
import re
import psutil
import shutil
import hashlib

'''
@author: github/wolverinn
@date: 03/22/2019

requirements:
    Python 3.x
    psutil
    setting.json

function：
Sync the files on computer to portable devices, including auto-update and deletion.

待改进：setting.json 可以直接放在U盘的同步文件夹中。setting.json可以直接不要U盘文件夹这一项，直接硬编码
'''

'''
setting.json:
At the minimum, you need to complete the "computer_locations"

"computer_locations" is a list of locations in your computer that you want to sync
"portable_device_folder" is the location in the portable device where your sync folder exists, you can also leave it blank and a default sync folder will be created automatically
"ignore" is a list of suffixs to exclude those you don't want to sync
"override_updates": "y" means when some files have changed, it will be automatically updated without asking; "n" means otherwise
"override_delete": "y" means when some files no longer exist on the computer, automatically delete the files in the portable device without asking
'''

'''
先设置电脑中需要同步的文件夹的绝对路径
对应的U盘路径如果不设置则会自动检测U盘然后创建同步文件夹
ignore填文件后缀名，出现在ignore中的文件后缀不会同步
override_updates表示需要更新时是否询问
override_delete表示需要删除时是否询问
'''

sync_folder = ""    # 移动设备的同步文件夹路径
portable_part = ""  # 移动设备的盘符
global dir_list # 需要同步的所有文件夹(包括子文件夹)

# 获取移动设备的盘符，以及判断是否有移动设备插入，如没有则推出
disk = psutil.disk_partitions()
for single_disk in disk:
    attr = single_disk.opts.split(",")
    if "fixed" not in attr and "cdrom" not in attr:
        portable_part = single_disk.device[:2] + "/"
if portable_part is "":
    print("no portable device detected!")
    os.system("pause")
    exit(1)

def right_dir(location):
    # 将目录统一格式为：<E:/dir/subdir/>，同时返回当前文件夹的名称
    try:
        right_location = location.replace("\\","/")
    except:
        pass
    if right_location[-1] is not "/":
        right_location = right_location + "/"
    locs = right_location.split("/")
    folder_name = locs[-2]
    return folder_name,right_location

def list_all_dir(upper_dir,location):
    # 返回当前目录下的所有文件夹，以子目录的形式装在全局变量dir_list中
    global dir_list
    temp_list = []
    temp_upper = []
    for item in os.listdir(location):
        if os.path.splitext(item)[1] is "":
            temp_item = upper_dir + item + "/"
            temp_list.append(item + "/")
            temp_upper.append(temp_item)
            dir_list.append(temp_item)
    if len(temp_list) == 0:
        return
    else:
        for i,ti in enumerate(temp_list):
            new_location = location + ti
            list_all_dir(temp_upper[i],new_location)
    return

def file_only_process(com_location,port_location):
    '''
    对于每一个目录，同步目录下的文件
    1. 如果文件不是文件夹且不在“ignore”中，则进行同步
    2. 如果移动设备中的文件不在电脑上，则询问删除
    3. 如果电脑上的文件不在移动设备上，则进行复制
    4. 如果一个文件同时在电脑和移动设备上，则比较MD5码，若不同则询问更新
    '''
    try:
        os.mkdir(port_location)
    except:
        pass
    port_files = os.listdir(port_location)
    for item in os.listdir(com_location):
        item_app = os.path.splitext(item)[1]
        if item_app is not "" and item_app not in setting["ignore"]:
            if item in port_files:
                f_port = open(port_location+item,'rb')
                f_com = open(com_location+item,'rb')
                md5_port = hashlib.md5(f_port.read()).hexdigest()
                md5_com = hashlib.md5(f_com.read()).hexdigest()
                f_port.close()
                f_com.close()
                if str(md5_port) != str(md5_com):
                    if setting["override_updates"] is "y" or setting["override_updates"] is "Y":
                        shutil.copyfile(com_location+item,port_location+item)
                    else:
                        ask_update = input(port_location+item+" has been changed in the computer, update? y/n ")
                        if ask_update is "y" or ask_update is "Y":
                            shutil.copyfile(com_location+item,port_location+item)
            else:
                shutil.copyfile(com_location+item,port_location+item)
    for item in port_files:
        if item not in os.listdir(com_location):
            if setting["override_delete"] is "y" or setting["override_delete"] is "Y":
                os.remove(port_location+item)
            else:
                ask_delete = input(port_location+item+" no longer exists in the computer, delete? y/n ")
                if ask_delete is "Y" or ask_delete is "y":
                    os.remove(port_location+item)


try:
    # 检查setting.json是否可以使用，否则退出
    with open("setting.json",'r') as f:
        # 检查是否指定了移动设备上的同步文件夹，若没有则默认创建
        # 检查指定的同步文件夹是否有效
        setting = json.load(f)
        if setting["portable_device_folder"] is "":
            print("No folder on the portable device is assigned")
            print("creating a sync folder {}sync/ in the portable device by default...".format(portable_part))
            sync_folder = portable_part+"sync/"
            try:
                os.mkdir(sync_folder)
            except:
                print("sync folder already exists on the portable device")
        else:
            sync_folder = setting["portable_device_folder"]
            _,sync_folder = right_dir(sync_folder)
            try:
                os.mkdir(sync_folder)
            except:
                pass
            try:
                os.listdir(sync_folder)
            except:
                print("The folder: {} doesn't exist".format(sync_folder))
                print("check the settings")
                os.system("pause")
                exit(1)
except:
    print("setting.json required")
    os.system("pause")
    exit(1)

for i,location in enumerate(setting["computer_locations"]):
    # 同步所有电脑上的文件夹中的文件
    # 先获取所有的次级目录
    print("syncing location: {} ...".format(location))
    global dir_list
    dir_list = [""]
    try:
        all_files = os.listdir(location)
    except:
        print("location:{} doesn't exist on the computer".format(location))
        print("skipping this location...")
        continue
    folder_name,location = right_dir(location)
    list_all_dir("",location)
    portable_location = sync_folder + folder_name + "/"
    try:
        os.mkdir(portable_location)
    except:
        pass
    for single_location in dir_list:
        print("    syncing /{}".format(single_location))
        com_location = location + single_location
        port_location = portable_location + single_location
        file_only_process(com_location,port_location)

os.system("pause")