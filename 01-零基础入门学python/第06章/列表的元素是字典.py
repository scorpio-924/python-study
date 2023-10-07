# 学生信息字典的列表，表达很多个学生信息
students = [
			{"id":101,"name":"xiaozhang","grade":88},
			{"id":102,"name":"xiaowang","grade":99},
			{"id":103,"name":"xiaoli","grade":77},
			{"id":104,"name":"xiaozhao","grade":86},
]

for student in students:
	id,name,grade = student["id"],student["name"],student["grade"]
	print(f"学号为{id}的姓名是{name}，成绩是{grade}分")