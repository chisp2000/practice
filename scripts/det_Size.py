import os

directory = '/home/kali/Downloads/'
file_path = os.scandir(directory)





def sizeRETURN():

    for filename in file_path:
        f = os.path.join(directory, filename)
        s = os.path.getsize(f)

        if os.path.isfile(f):
            print(f, s, "bytes")


print(sizeRETURN())

#sizeRETURN()
