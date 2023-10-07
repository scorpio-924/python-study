number = input("请输入一个数字:")

number = int(number)
if number % 2 == 0:
    print(f"你输入的是{number}，它是一个偶数")
else:
    print(f"你输入的是{number}，它是一个奇数")