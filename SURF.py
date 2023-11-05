import os
import shutil
import sys

#arrays
documentArray=["txt", "doc", "docx", "pdf", "ppt", "pptx", "html", "htm", "epub", "xopp", "odt"]
imageArray=["jpg", "jpeg", "png", "heic", "webp", "gif"]
videoArray=["mp4", "mov", "avi", "wmv", "webm", "flv", "ogv"]
musicArray=["mp3", "wav", "alac", "flac", "wma", "m4a", "aiff"]


if len(sys.argv) < 2:
    file_path = "Downloads"
else:
    file_path = sys.argv[1]
    print("File path:", file_path)

filelist = []
#toggle this with the recursive flag
#def list_files_recursively(directory):
#    for root, dirs, files in os.walk(directory):
#        for file in files:
#            file_path = os.path.join(root, file)
#            filetree.append(file_path)
#list_files_recursively(file_path)
filelist = os.listdir(file_path)
for file in filelist:
    if file[0] == '.':
        continue
    split_string = file.rsplit(".", 1)
    if len(split_string)==1:
        continue
    filename = split_string[0]
    extension = split_string[1]
    outputname = file.split('/')[-1]
    if extension in documentArray:
        print(outputname + " is going to the documents folder")
    elif extension in imageArray:
        print(outputname + " is going to the pictures folder")
    elif extension in videoArray:
        print(outputname + " is going to the videos folder")
    elif extension in musicArray:
        print(outputname + " is going to the music folder")
    else:
        print(outputname + " is going to the shadow realm")