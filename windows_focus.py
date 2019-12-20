import os
import shutil
from PIL import Image
import getpass

'''
@author: github/wolverinn
@date: 08/03/2018

requirements:
- Python 3.x
- Pillow

Function:
Save Windows-Focus images to a folder. Original Windows-Focus images: 
- don't have a right image format with ".jpg" or ".png".
- image sizes are mixed in a large number of images.
- are in a location very hard to find.
'''

try:
    os.mkdir("./windows-focus")
except:
    pass

focus_loc="C:/Users/"+str(getpass.getuser())+"/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"
for files in os.listdir(focus_loc):
    new_file="./windows-focus/"+str(files)
    old_file="C:/Users/"+str(getpass.getuser())+"/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets/"+str(files)
    shutil.copyfile(old_file,new_file)

os.chdir("./windows-focus")
for file in os.listdir("./windows-focus"):
    if len(str(file).split(".")) is 1:
        new_name=str(file)+".jpg"
        try:
            os.rename(file,new_name)
        except:
            os.remove(file)
    else:
        new_name=file
    img=Image.open(new_name)
    h=img.size[1]
    w=img.size[0]
    if w<1920:
        img.close()
        os.remove(new_name)
        # print("h:",h,";w:",w)

print("All the images have been save to ./windows-focus")
os.system("pause")
