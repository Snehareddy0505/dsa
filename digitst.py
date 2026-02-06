def st(s):
    res="" 
    i=0
    while i<len(s):
        if s[i].isdigit():
            num=0
            while i<len(s) and s[i].isdigit():
                num=num*10+int(s[i])
                i+=1
            if i<len(s):
                res+=s[i]*num
                i+=1
        else:
            res+=s[i]
            i+=1
    return res
