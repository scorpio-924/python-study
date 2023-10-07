import os
import string

if not os.path.exists("p054"):
	os.makedirs("p054")
for letter in string.ascii_lowercase:
	with open(f"p054/{letter}.txt","w") as f:
		f.write(letter)