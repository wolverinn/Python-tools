import os
import getpass
import shutil

'''
@author: github/wolverinn
@date: 08/10/2018

requirements:
- Python 3.x

function:
Edit the send-to options in Windows when you right-click a file/folder.
You can remove the existing options, or add a shortcut/program as the send-to option.

这个程序最好做成图形操作界面
TODO: make a GUI for this program
'''

sendto="C:/users/"+str(getpass.getuser())+"/AppData/Roaming/Microsoft/Windows/SendTo"
def remv():
    for i, file in enumerate(os.listdir(sendto)):
        print(str(i), end='.')
        print(file)
    num=input("input the number of the object you want to remove from send-to(multiple objects should be seperated by \';\'):")
    try:
        num=num.split(';')
    except:
        return
    for i, file in enumerate(os.listdir(sendto)):
        if str(i) in num:
            remv_file=sendto+"/"+str(file)
            os.remove(remv_file)
            print(file,"removed")

def loc(add,app=''):
    if app is not '':
        app="/"+app
    add=add+app
    shortcutname = input("name the shortcut:")
    f = open("temp.vbs", 'w')
    f.write("set WshShell = WScript.CreateObject(\"WScript.Shell\")\n")
    shortcutname = "\"" + shortcutname + ".lnk\""
    temp = "set oShellLink = WshShell.CreateShortcut(" + shortcutname + ")\n"
    f.write(temp)
    temp = "oShellLink.TargetPath = \"" + add + "\"\n"
    f.write(temp)
    f.write("oShellLink.WindowStyle = 1\n")
    temp = "oShellLink.WorkingDirectory =\"" + add + "\"\n"
    f.write(temp)
    temp = "oShellLink.IconLocation = \"" + add + ",0\"\n"
    f.write(temp)
    f.write("oShellLink.Save\n")
    f.close()
    os.system("temp.vbs")
    os.remove("temp.vbs")
    for file in os.listdir():
        if str(file).split('.')[-1] == "lnk":
            shutil.move(file, sendto)
    print("added successfully")

while(True):
    print("1) remove elements of send-to;")
    print("2) add a location to send-to;")
    print("3) add an application to send-to")
    option=input("your option(1/2/3):")
    if option=="1":
        remv()
    elif option=="2":
        location=input("add location:")
        loc(location)
    elif option=="3":
        location = input("add location of the application:")
        app = input("application name(including .exe):")
        loc(location,app)
    else:
        print("invalid option")