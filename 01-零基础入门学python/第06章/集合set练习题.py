# 字典的value是列表，表达每个人列表类型信息
students = {
			"xiaozhang":["足球","篮球"],
			"xiaowang":["篮球","乒乓球"],
			"xiaozhang":["篮球","棒球","台球"],
			"xiaozhao":["乒乓球","羽毛球"]
}
likes = set()
for value in students.values():
    for like in value:
        likes.add(like)
print(likes)