import os

dir = r"D:\.aa-刘天天的文件夹\刘天天\蚂蚁python\蚂蚁学python\02-python编程练习100题\第16章"
for root,dirs, files in os.walk(dir):
	for file in files:
		fpath = os.path.join(root,file)
		print(fpath)
