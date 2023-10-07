# 学生信息字典的列表，表达很多个学生信息
students = {
			"xiaozhang":{"id":101,"grade":88},
			"xiaowang":{"id":102,"grade":99},
			"xiaoli":{"id":103,"grade":77},
			"xiaozhao":{"id":104,"grade":86},
}

for name,info in students.items():
	id,grade = info["id"],info["grade"]
	print(f"姓名为{name}，学号为{id}，成绩是{grade}分")