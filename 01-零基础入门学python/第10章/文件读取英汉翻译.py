
eng_dict = {}
with open("英汉词典.txt", encoding="utf8") as f:
    for line in f:
        line = line.rstrip()
        fields = line.rsplit("，")
        if len(fields) != 2:
            continue
        english,chinese = fields
        eng_dict[english] = chinese

while True:
    print("#" * 20)
    info = input("请输入英文词语：")
    if info == "quit":
        break

    if info in eng_dict:
        print("查询结果，汉语是：",eng_dict[info])
    else:
        print("没有这个词语：",info)


