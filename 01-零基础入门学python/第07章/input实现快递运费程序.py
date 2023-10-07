while True:
    print("#" * 20)
    weight = input("请输入商品数量：")
    if weight == "quit":
        break
    else:
        weight = float(weight)

        if weight <= 0:
            print("输入错误，你输入的是0或者负数")
            continue

        if 0< weight <= 1:
            print("金额是：7元")

        elif 1<weight<3:
            print("金额是：",(7 + 2*weight))
        else:
            print("金额是：", (7 + 2 * weight))

