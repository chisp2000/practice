

def enter_header():
    header = str(input("\nEnter your title: "))
    return header

def enter_content():
    content1 = str(input("\nEnter your content: "))
    return content1

def chooseAmount_p():
    inpat = input("\nHow many paragraphs would you like to write? (DEFAULT:1)")
    if type(inpat) == type(3):
        return inpat
    elif inpat == "DEFAULT":
        return 1
    else:
        print("The value you entered is invalid.")
        return 1

def chooseAmount_h():
    inpat = input("\nHow many headers would you like to write? (DEFAULT:1)")
    if type(inpat) == type(3):
        return inpat
    elif inpat == "DEFAULT":
        return 1
    else:
        print("The value you entered is invalid.")
        return 1



def openFile(HEADER, CONTENT, AMOUNT_H, AMOUNT_P):
    file = open("website.html", "w")
    web_array = []
    for i in range(0, (AMOUNT_H+1)):
        web_array.append("<h1>")
        web_array.append(HEADER)
        web_array.append("</h1>")

    for i in range(0, (AMOUNT_P+1)):
        web_array.append("<p>")
        web_array.append(CONTENT)
        web_array.append("</p>")

    tot_website = ''.join(web_array)


    file.write(tot_website)
    file.close()






h = enter_header()
c = enter_content()
ah = chooseAmount_h()
ap = chooseAmount_p()

openFile(h, c, ah, ap)
