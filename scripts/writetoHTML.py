

writtenword = ""


def choose_style():
    take = str(input("\nEnter the style you wish to use: "))
    return take


def enter_info():
    writtenWord = str(input("\nEnter your string: "))
    return writtenWord

def openFile(styles, infos):
    file = open("website.html", "w")

    styleBRACKETSopen = "<%s>" % (styles)
    styleBRACKETSclosed = "</%s>" % (styles)
    stringTOWEB = (styleBRACKETSopen, infos, styleBRACKETSclosed)

    #file.write(stringTOWEB)
    file.write("<%s>%s</%s>" % (styles, infos, styles))
    file.close()

style = choose_style()
info = enter_info()

openFile(style, info)
