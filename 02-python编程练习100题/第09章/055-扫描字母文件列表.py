import glob

letters = []
file_list = glob.glob("p054/*.txt")

for file in file_list:
	with open(file) as f:
		letters.append(f.read().strip())
print(letters)