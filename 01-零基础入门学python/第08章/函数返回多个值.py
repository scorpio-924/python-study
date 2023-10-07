students = {
			"xiaoming":{"id":101,"age":18,"gender":"boy"},
			"xiaohuang":{"id":102,"age":19,"gender":"girl"},
			"xiaowang":{"id":103,"age":17,"gender":"girl"},
}

def get_student(name):
	if name in students:
		return students[name]["age"],students[name]["gender"]
	else:
		return None,None
age,gender = get_student("xiaohuang")
info = get_student("xiaoxiaoxiao")

print(age,gender)
print(info,type(info))