import pandas as pd


datas =[]
while True:
    print("#"*20)
    info = input("请输入姓名和金额：")
    if info == "quit":
        break
    fields = info.split()
    if len(fields) != 2:
        print("输入有问题，请再次输入")
        continue
    name,money = fields
    datas.append([name,money])

df = pd.DataFrame(datas,columns=["姓名","金额"])

df.to_excel("婚礼礼金结果.xlsx",index=False)