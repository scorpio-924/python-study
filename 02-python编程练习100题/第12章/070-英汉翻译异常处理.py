d = {"apple":"苹果","orange":"桔子","banana":"香蕉"}

def translate(word):
	try:
		return d[word]
	except KeyError:
		return "单词不在词典中"

word = input("Enter word: ")
print(translate(word))