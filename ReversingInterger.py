
def reverseInt(num):
	reverse = 0 
	while num > 0:
		remainder = num%10
		reverse = reverse*10 + remainder
		num = num//10
	return reverse


num = 1234
y = 4321

print(reverseInt(y))