

def enter_header():
    header = str(input("\nEnter your title: "))
    return header

def enter_content():
    content1 = str(input("\nEnter your content: "))
    return content1

def chooseAmount_p():
    input = input("\nHow many paragraphs would you like to write? (DEFAULT:1)")
    if type(input) == type(3):
        return input
    elif input == "DEFAULT":
        return 1
    else:
        print("The value you entered is invalid.")
        return 1

def chooseAmount_h():
    input = input("\nHow many headers would you like to write? (DEFAULT:1)")
    if type(input) == type(3):
        return input
    elif input == "DEFAULT":
        return 1
    else:
        print("The value you entered is invalid.")
        return 1



def openFile(HEADER, CONTENT, AMOUNT_H, AMOUNT_P):
    file = open("website.html", "w")
    tot_website = []
    for i in range(0, (AMOUNT_H+1)):
        tot_website.append("<h1>")
        tot_website.append(HEADER)
        tot_website.append("</h1>")

    for i in range(0, (AMOUNT_P+1)):
        tot_website.append("<p>")
        tot_website.append(CONTENT)
        tot_website.append("</p>")


    file.write(tot_website)
    file.close()






h = enter_header()
c = enter_content()
ah = chooseAmount_h()
ap = chooseAmount_p()

openFile(h, c, ah, ap)
