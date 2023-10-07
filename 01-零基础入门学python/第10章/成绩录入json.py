
import os
import json
file_name = "成绩录入json.txt"
grade_dict = {}
if os.path.exists(file_name):
    with open(file_name,encoding="utf8") as f:
        grade_dict = json.loads(f.read())
print("### 读取文件后的内容")
for key,value in grade_dict.items():
    print(key,value)


while True:
    print("#"*20)
    info = input("请输入姓名和成绩：")
    if info == "quit":
        break
    fields = info.split()
    if len(fields) != 2:
        continue
    name,grade = fields
    grade = int(grade)
    grade_dict[name] = grade

with open(file_name,"w",encoding="utf8") as f:
    f.write(json.dumps(grade_dict))
