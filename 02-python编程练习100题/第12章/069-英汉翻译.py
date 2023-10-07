d = {"apple":"苹果","orange":"桔子","banana":"香蕉"}

def translate(word):
	return d[word]
word = input("Enter word: ")
print(translate(word))