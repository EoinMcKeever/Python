x = "radar"
y = "madam"
z = "hjdi"

def palindrome(word):
	if word != word[::-1]:
		return "Not a palindrome"
	else:
		return "Word is a palindrome"		
print(palindrome(x))
