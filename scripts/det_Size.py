import os
from humanize import naturalsize

directory = input("Please enter the directory you'd like to search: ")
xsize = int(input("Please input which size you would like to search for: "))


def sizeRETURN():
    #looks for files in directory variable
    for (root,dirs, files) in os.walk(directory, onerror=None):
        #looks through each file in files
        for name in files:
            #path is the full path of the searched file
            path = os.path.join(root, name)
            #checks if file in path exists
            isFile = os.path.isfile(path)
            #checks if isFile is  true and also larger than xsize
            if isFile and (os.stat(path).st_size >= xsize):
                print(path, naturalsize(os.stat(path).st_size), "bytes")

sizeRETURN()
