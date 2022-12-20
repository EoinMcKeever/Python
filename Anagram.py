x = "restful"
y = "fluster"

def Anagram(word1,word2):
	word1 = sorted(word1)
	word2 = sorted(word2)
	if word1 == word2:
		return "Anagram"
	else:
		return "Not Anagram"

print(Anagram(x,y))			

