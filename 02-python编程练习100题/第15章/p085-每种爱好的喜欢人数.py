like_count = {}

with open("p085.txt",encoding="utf8") as fin:
	for line in fin:
		line = line[:-1]
		sname,likes = line.split(" ")
		like_list = likes.split(",")
		for like in like_list:
			if like not in like_count:
				like_count[like] = 0
			like_count[like] += 1
for key,value in like_count.items():
	print(key,value)