from collections import Counter
def isValid(s):
    # Write your code here
	d = Counter(s)
	d = Counter(str(s))
	print(d["a"])

	print(d)
	if len(d) == 1:
		return "YES"
		if len(d) > 2:
			return "NO"	

	print(d)
	if 1 in d.values() and (d[min(d.keys())]==1 or (max(d.keys()) - min(d.keys())==1)):
		return "YES"
	else:
		return "NO"
                    
            
isValid("aaaabbcc")       




