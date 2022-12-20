def sherlockAndAnagrams(s):
    dic = {}
    ic = []
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            ic.append (s[j:j+i])
    return(ic)        
            