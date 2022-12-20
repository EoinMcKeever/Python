x = [1,2,3,4,5,6,7,8,9]

def reverse(list):
	for i in range(len(list)//2):
		list[i],list[-i-1] = list[-i-1],list[i]
	return list
#print(reverse(x))	
