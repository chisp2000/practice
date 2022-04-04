def validPalindrome(s):

    failstring = False

    if len(s) >= pow(10,5):
        failstring = False
    else:
        if s == s[::-1]:
            failstring = True
        if failstring == False:
            for i in range(len(s)):
                q = s[:i] + s[i+1:]
                if q == q[::-1]:
                    failstring = True


    return failstring
