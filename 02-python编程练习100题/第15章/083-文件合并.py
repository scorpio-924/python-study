with open("p083.txt","w",encoding="utf8") as fout:
	for fname in ["p083_xiaomei.txt","p083_xiaohua.txt"]:
		with open(fname,encoding="utf8") as fin:
			for line in fin:
				fout.write(line)