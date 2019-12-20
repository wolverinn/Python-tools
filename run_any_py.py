import os

'''
@author: github/wolverinn
@date: 01/23/2019

requirements: None

function: if you have lots of python files in a directory, you can run this script to choose a .py file to run
'''

py_files = []
for all_file in os.listdir():
    if ".py" in all_file:
        py_files.append(all_file)

for i,a in enumerate(py_files):
    print(str(i),a)

choice = input("which one do you want to python it?")
try:
    ch_num = int(choice)
except:
    print("did you make a tiny mistake or did it deliberatly???")
if ch_num>=len(list(py_files)):
    print("OF!!")
else:
    os.system("python "+list(py_files)[ch_num])

os.system("pause")