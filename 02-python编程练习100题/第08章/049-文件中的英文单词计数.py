def count_words(filepath):
	with open(filepath,"r") as file:
		string = file.read()
		string_list = string.split(" ")
		print(string_list)
		return len(string_list)
print(count_words("p049.txt"))
