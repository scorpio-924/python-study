
import random
target = random.randint(0,100)
# print("target:",target)

count = 1
success = False
while count <= 10:
    print(("#"*20))
    number = input(f"第{count}次，请输入一个数字：")
    if not str(number).isnumeric():
        print("你输入的不是数字，请继续")
        continue
    number = int(number)
    if number == target:
        print("恭喜你才对了，数字是：",target)
        success = True
        break
    elif number < target:
        print("你猜的小了")
    else:
        print("你猜的大了")

    count += 1
if not success:
    print("很遗憾你没有才对，正确数字是：",target)



