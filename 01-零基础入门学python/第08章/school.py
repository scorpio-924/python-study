import student_query

while True:
    print("#"*20)
    name = input("请输入学生姓名：")
    if name == "quit":
        break
    info = student_query.get(name)
    if info:
        print("查到了，信息是：",info)
    else:
        print("没有这个学生的信息")


