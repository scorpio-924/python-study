import glob

letters = []
file_list = glob.glob("p054/*.txt")

for file in file_list:
	with open(file) as f:
		letter = f.read().strip()
	if letter in "python":
		letters.append(letter)
print(letters)