import os

directory = "/home/kali/Desktop/"


def sizeRETURN():

    for (root,dirs, files) in os.walk(directory, followlinks=True):
        print(os.path.abspath(""))
        for name in files:
            print(name)
            print(os.path.getsize(name))
            #if os.path.getsize(name) > 1000000000:
            #path = (os.path.join(root, name))
            #size = os.path.getsize(path)



sizeRETURN()
