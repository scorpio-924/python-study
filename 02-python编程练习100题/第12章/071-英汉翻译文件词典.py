engdict = {}
with open("p071.txt", encoding="utf8") as f:
	for line in f:
		eng,ch = line.strip().split("，")
		engdict[eng] = ch

def translate(word):
	try:
		return engdict[word]
	except KeyError:
		return "单词不在词典中"

word = input("Enter word: ").lower()
print(translate(word))