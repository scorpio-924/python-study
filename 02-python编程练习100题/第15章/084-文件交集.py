def get_aihao(fname):
	aihao = []
	with open(fname,encoding="utf8") as f:
		for line in f:
			aihao.append(line.split()[1])
	return aihao
xiaomei = get_aihao("p084_xiaomei.txt")
xiaohua = get_aihao("p084_xiaohua.txt")
for i in set(xiaomei).intersection(set(xiaohua)):
	print(i)