import os
from tkinter import *
from tkinter import filedialog,messagebox

def choose_file():
    filename = filedialog.askopenfilename()
    # filename = filedialog.askdirectory()
    if filename != '':
        l3.config(text = filename)
        b3['state'] = 'normal'
    else:
        l3.config(text = "(您没有选择任何文件)")
def choose_directory():
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    if filename != '':
        l3.config(text = filename)
        b3['state'] = 'normal'
    else:
        l3.config(text = "(您没有选择任何文件(夹))")

def choose_directory1():
    # filename = filedialog.askopenfilename()
    filename = filedialog.askdirectory()
    if filename != '':
        l7.config(text = filename)
        b5['state'] = 'normal'
    else:
        l7.config(text = "(您没有选择任何路径)")

def hide_file():
    filename = l3["text"]
    # print(filename)
    hide_cmd = "attrib +s +a +h +r "+filename
    os.system(hide_cmd)
    b3['state'] = DISABLED
    l3.config(text = "(您没有选择任何文件(夹))")
    messagebox.showinfo('提示','hide ok')

def unhide():
    filename = e1.get()
    filepath = l7["text"]
    unhide_cmd = "attrib -s -a -h -r "+filepath+'\\'+filename
    os.system(unhide_cmd)
    b5['state'] = DISABLED
    l7.config(text = "(您没有选择任何路径)")
    messagebox.showinfo('提示','unhide ok')

root = Tk()
root.geometry("320x480")
root.wm_title("file hidder")
l_hide = Label(root,text="********HIDE********")
b1 = Button(root,text="选择文件",command=choose_file)
l1 = Label(root,text = '或')
b2 = Button(root,text="选择文件夹",command=choose_directory)
l2 = Label(root,text='你选择的是')
l3 = Label(root,text="(您没有选择任何文件(夹))")
b3 = Button(root,text="confirm hide",state=DISABLED,command=hide_file)
l4 = Label(root,text="----------------------------------------------------------")
l5 = Label(root,text="tips:在浏览器中打开路径可查看隐藏文件")
l6 = Label(root,text="----------------------------------------------------------")
l_unhide = Label(root,text="********UNHIDE********")
b4 = Button(root,text="选择文件或文件夹所在路径",command=choose_directory1)
l7 = Label(root,text='')
l8 = Label(root,text="输入文件或文件夹名")
e1 = Entry(root)
b5 = Button(root,text="unhide",state=DISABLED,command=unhide)

l_hide.pack()
b1.pack()
l1.pack()
b2.pack()
l2.pack()
l3.pack()
b3.pack()
l4.pack()
l5.pack()
l6.pack()
l_unhide.pack()
b4.pack()
l7.pack()
l8.pack()
e1.pack()
b5.pack()
root.mainloop()