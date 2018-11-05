import os
import time
import random
from os import listdir
from os.path import isfile, join
from random import randint
from InstagramAPI import InstagramAPI

PhotoPath = "/home/irakli/Desktop/Image"  # Change Directory to Folder with Pics that you want to upload
IGUSER = "USERNAME"  # Change to your Instagram USERNAME
PASSWD = "Password"  # Change to your Instagram Password
# Change to your Photo Hashtag
IGCaption = "Follow Our best Page and <3  @programmer___humor <3 code #coders #programming #programmer #programmingmemes #python #pycoders #javascript #java #csharp #programming #programmingmemes #programmer___humor #programmers_life #hacker #hacking #programminglife #programmerhumor"
os.chdir(PhotoPath)
ListFiles = sorted([f for f in listdir(PhotoPath) if isfile(join(PhotoPath, f))])
print(ListFiles)
print("Total Photo in this folder:" + str(len(ListFiles)))

# #Start Login and Uploading Photo
igapi = InstagramAPI(IGUSER, PASSWD)
igapi.login()  # login

for i, _ in enumerate(ListFiles):
    photo = ListFiles[i]
    print("Progress :" + str([i + 1]) + " of " + str(len(ListFiles)))
    print("Now Uploading this photo to instagram: " + photo)
    igapi.uploadPhoto(photo, caption=IGCaption, upload_id=None)
    os.remove(photo)
    # sleep for random between 60 - 120s
    n = randint(700,900)
    print("Sleep upload for seconds: " + str(n))
    time.sleep(n)