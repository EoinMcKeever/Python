def sherlockAndAnagrams(s):
    dic = {}
    ic = []
    for i in range(1,len(s)):
        for j in range(0,len(s)-i+1):
            ic.append("".join(sorted(s[j:j+i])))
    count = {k:v for k,v in Counter(ic).items() if v>1} 
    total = 0
    for i in count.values():
        total += sum(range(i))
    return total
            