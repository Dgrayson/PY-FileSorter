__author__ = 'dgrayson'

from os import rename
from os import listdir

def main():

    doc_types = ['pdf', 'txt', 'doc', 'docx', 'ppt', 'pptx']
    pic_types = ['jpg', 'gif', 'png', 'tiff', 'exif', 'bmp']
    mus_types = ['mp3', 'wav', 'mid', 'flac']
    vid_types = ['mp4', 'mkv', 'webm', 'flv', 'avi', 'wmv', ]

    pc_user = input("Please enter the name of the user folder: ")

    source = "C:/Users/" + pc_user + "/Downloads"

    doc_dest = "C:/Users/" + pc_user + "/Documents"
    pic_dest = "C:/Users/" + pc_user + "/Pictures"
    mus_dest = "C:/Users/" + pc_user + "/Music"
    vid_dest = "C:/Users/" + pc_user + "/Videos"

    files = [f for f in listdir(source)]

    for i in files: 

        type = parseFile(i)

        print(type)

        if type in doc_types: 
            print("Sent to docs\n")
        elif type in pic_types: 
            print("Sent to pics\n")
        elif type in mus_types: 
            print("Sent to music\n")
        elif type in vid_types: 
            print("Sent to Videos\n")
        elif type == None: 
            print("Directories cannot be moved\n")



def parseFile(f):

    print(f)

    fileType = f.split(".")

    length = len(fileType)

    if length > 1: 
        return fileType[1]
    else: 
        return None

def moveFile(s, d):

    print("hello")

if __name__ == "__main__":
    main()
