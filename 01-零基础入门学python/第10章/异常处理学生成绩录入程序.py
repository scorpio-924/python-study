

file_name = "学生成绩带异常处理.txt"
with open(file_name,"w",encoding="utf8") as f:
    while True:
        print("#"*20)
        info = input("请输入姓名和成绩：")
        try:
            if info == "quit":
                break
            name,grade = info.split()

            grade = int(grade)
        except Exception as e:
            print("出现问题了：",e,"你输入的是：",info)
            continue
        f.write(f"{name},{grade}\n")
print("success")
