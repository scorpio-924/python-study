# 创建多个人的成绩数据
grades = {"小明":88,"小花":99,"小张":77,"小白":85}

for name in grades.keys():
#可以只使用key，也可以用字典的方式获得value
	print(name,grades[name])