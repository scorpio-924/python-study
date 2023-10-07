import string
with open("p052.txt","w") as f:
	for i,j in zip(string.ascii_lowercase[::2],string.ascii_lowercase[1::2]):
		f.write(i + j + "\n")