

writtenword = ""


def enter_header():
    header = str(input("\nEnter your title: "))
    return header

def enter_content():
    content1 = str(input("\nEnter your content: "))
    return content1



def openFile(i, c):
    file = open("website.html", "w")
    file.write("<h1>%s</h1><p>%s</p>" % (i, c))
    file.close()



info = enter_header()
content = enter_content()

openFile(info, content)
