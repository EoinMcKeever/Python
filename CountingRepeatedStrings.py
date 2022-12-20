def repeatedString(s, n):
    c = s.count('a')
    div=n//len(s)
    if n%len(s)==0:
        c= c*div
    else:
        m = n%len(s)
        c= c*div+s[:m].count('a')
    return c
