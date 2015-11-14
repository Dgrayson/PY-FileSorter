__author__ = 'dgrayson'

import os
from os import rename
from os import listdir

def main():

    doc_types = ['pdf', 'txt', 'doc', 'docx', 'ppt', 'pptx']
    pic_types = ['jpg', 'gif', 'png', 'tiff', 'exif', 'bmp']
    mus_types = ['mp3', 'wav', 'mid', 'flac']
    vid_types = ['mp4', 'mkv', 'webm', 'flv', 'avi', 'wmv', ]

    pc_user = input("Please enter the name of the user folder: ")

    source = "C:/Users/" + pc_user + "/Desktop"

    doc_dest = "C:/Users/" + pc_user + "/Documents"
    pic_dest = "C:/Users/" + pc_user + "/Pictures"
    mus_dest = "C:/Users/" + pc_user + "/Music"
    vid_dest = "C:/Users/" + pc_user + "/Videos"

    files = [f for f in listdir(source)]

    for i in files: 

        type = parseFile(i)

        if type in doc_types: 
            print("Sent to docs\n")
            moveFile(i, doc_dest, source)
        elif type in pic_types: 
            print("Sent to pics\n")
            moveFile(i, pic_dest, source)
        elif type in mus_types: 
            print("Sent to music\n")
            moveFile(i, mus_dest, source)
        elif type in vid_types: 
            print("Sent to Videos\n")
            moveFile(i, vid_dest, source)
        elif type == None: 
            print("Directories cannot be moved\n")
        else: 
            print("Invalid file type, File not moved")



def parseFile(f):

    print(f)

    fileType = f.split(".")

    if len(fileType) > 1: 
        return fileType[1]
    else: 
        return None

def moveFile(i, d, s):

    dest_files = [f for f in listdir(d)]

    destination = d + "/" + i
    source = s + "/" + i

    if not os.path.isfile(destination): 
        os.rename(source, destination)
    else: 
        print("File already exists in destination")

    

if __name__ == "__main__":
    main()
