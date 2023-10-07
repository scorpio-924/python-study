student = (1001,'xiaoming',20,176)
print(student,type(student))


for x in student:
    print(x)

print("拆包的得到多个变量：")
学号,姓名,年龄,身高 =student
print("学号：",学号)
print("姓名：",姓名)
print("年龄：",年龄)
print("身高：",身高)

student = (1002,'xiaobai',21,173)
print("修改后：",student,type(student))
