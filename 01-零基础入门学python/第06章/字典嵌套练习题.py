
# 学生信息字典的列表，表达很多个学生信息
students = {
			"xiaozhang":{"id":101,"grade":88},
			"xiaowang":{"id":102,"grade":99},
			"xiaoli":{"id":103,"grade":77},
			"xiaozhao":{"id":104,"grade":86},
}
students["xiaoli"]["grade"] = 87
print(students)
grades =[]
for name,info in students.items():
    grades.append(info["grade"])

print(grades)
grades.sort(reverse=True)
print(grades)



