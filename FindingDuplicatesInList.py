
x = [1,2,3,1,5]

def Repition(list):
	for i in range(len(x)-1):
		if x[abs(x[i])] < 0:
			return str(abs(x[abs(x[i])])) + " repeated"
		else:
			x[abs(x[i])] = x[abs(x[i])] * -1
	return "No Repition"		


print(Repition(x))