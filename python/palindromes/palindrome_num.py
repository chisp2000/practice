
def validPal(s):
    failstring = False
    inputnum = s
    number_rev = 0

    while(inputnum > 0):
        remainder = inputnum % 10
        number_rev = (number_rev * 10) + remainder
        inputnum = inputnum // 10

    if s == number_rev:
        return True

    else: return False





print(validPal(13334531))
