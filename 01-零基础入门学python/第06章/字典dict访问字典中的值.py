user = {"id":123,"name":"小明","age":20}

print(user["id"])
print(user["name"])
print(user["age"])

# 如下如果写user["grade"] 会报错说 keyError：'grade'
# 写get就不会报错，也可以指定默认值
print(user.get("grade"))
print(user.get("grade",80))

# 创建多个人信息的字典
grades = {"小明":88,"小花":99,"小张":77,"小白":85}
print(grades)

# 如下两个，因为key不存在，会新增键值对
grades["小李"] = 90
grades["小赵"] = 88

# 如下一个，因为小张之前存在键，所以值会修改
grades["小张"] = 79

print(grades)