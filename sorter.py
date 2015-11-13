__author__ = 'dgrayson'

from os import rename
from os import listdir

def main():

    pc_user = input("Please enter the name of the user folder: ")

    source = "C:/Users/" + pc_user + "/Downloads"

    doc_dest = "C:/Users/" + pc_user + "/Documents"
    pic_dest = "C:/Users/" + pc_user + "/Pictures"
    mus_dest = "C:/Users/" + pc_user + "/Music"
    vid_dest = "C:/Users/" + pc_user + "/Videos"

    files = [f for f in listdir(source)]

    print(files)

    type = parseFile(files[0])

    print(type)

def parseFile(f):

        fileType = f.split(".")

        print(fileType[1])

        return fileType[1]

if __name__ == "__main__":
    main()
