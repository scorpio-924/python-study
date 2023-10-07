import re
def count_words(filepath):
	with open(filepath,"r") as file:
		string = file.read()
		string_list = re.split(r",| ",string)
		print(string_list)
		return len(string_list)
print(count_words("p050.txt"))