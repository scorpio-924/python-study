fname = "婚礼礼金.txt"
with open(fname,"w",encoding="utf8") as f:
    while True:
        print("#"*20)
        info = input("请输入来人和金额：")
        if info == "quit":
            break
        fields = info.split()
        if len(fields) == 2:
            name,money = fields
        else:
            continue
        money = int(money)
        f.write(f"{name},{money}\n")

with open(fname,encoding="utf8") as f:
    moneys = []
    for line in f:
        line = line[:-1]
        fields = line.split(",")
        if len(fields) == 2:
            name,money = fields
        else:
            continue
        moneys.append(int(money))
    print("加和：",sum(moneys))
    print("最大：",max(moneys))
    print("最小：",min(moneys))
    print("平均：",sum(moneys)/len(moneys))