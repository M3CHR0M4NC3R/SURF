import os
import shutil
import sys
import tkinter as tk

#Window
window = tk.Tk()
window.geometry('500x300')
window.title("S.U.R.F")
#arrays
documentArray=["txt", "doc", "docx", "pdf", "ppt", "pptx", "html", "htm", "epub", "xopp", "odt"]
imageArray=["jpg", "jpeg", "png", "heic", "webp", "gif"]
videoArray=["mp4", "mov", "avi", "wmv", "webm", "flv", "ogv"]
musicArray=["mp3", "wav", "alac", "flac", "wma", "m4a", "aiff"]


def organise_files (inputpath):
    filelist = []
    userfolder = os.path.expanduser('~')
    #toggle this with the recursive flag
    #def list_files_recursively(directory):
    #    for root, dirs, files in os.walk(directory):
    #        for file in files:
    #            file_path = os.path.join(root, file)
    #            filetree.append(file_path)
    #list_files_recursively(file_path)
    filelist = os.listdir(userfolder + '/' + inputpath)
    for file in filelist:
        if file[0] == '.':
            continue
        split_string = file.rsplit(".", 1)
        if len(split_string)==1:
            continue
        filename = split_string[0]
        extension = split_string[1]
        outputname = file.split('/')[-1]
        #have variable for user folder
        if extension in documentArray:
            print(outputname + " is going to the documents folder")
            shutil.move(userfolder+'/'+inputpath+'/'+file, userfolder + "/Documents")
        elif extension in imageArray:
            print(outputname + " is going to the pictures folder")
            shutil.move(userfolder+'/'+inputpath+'/'+file, userfolder + "/Pictures")
        elif extension in videoArray:
            print(outputname + " is going to the videos folder")
            shutil.move(userfolder+'/'+inputpath+'/'+file, userfolder + "/Videos")
        elif extension in musicArray:
            print(outputname + " is going to the music folder")
            shutil.move(userfolder+'/'+inputpath+'/'+file, userfolder + "/Music")
        else:
            print(outputname + " is going to the shadow realm")

title = tk.Label(window, text = "Please input the name of the folder \n you wish to sort.", font = 'Calibri 16 bold' )
title.pack()


#import file
#import SURF




def Button_click():
    title.config(text = "Yar, your files be sorted")
    #run the SURF command with the entry.get() as an argument, slap that bitch together like a string
    #yessur
    organise_files(entry.get())



#Inputs
input = tk.Frame(window)
entry = tk.Entry(input)
Button = tk.Button(input, text = "That Was Easy", command = Button_click)
entry.pack(side = 'left', padx = 10)
Button.pack(side = 'left')
input.pack(pady = 30)

#Output Label 
#Output = tk.Label(window, text = "OutPut")
#
#Output.pack()

window.mainloop()