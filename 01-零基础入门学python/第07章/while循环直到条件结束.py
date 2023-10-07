number,sum_value = 1,0

while number <= 100:   # 一直判断这个条件，直到不满足
	sum_value += number   # while的冒号下方，可以写多行语句
	number += 1      # 请注意循环条件变化，不然可能是死循环，永远不会结束
print(sum_value)

number,sum_value = 0,0

while True:
	number += 1

# 奇数，跳过不计算
	if number % 2 == 1:
		continue
	sum_value += number
	# 如果已经超过100了结束循环
	if number > 100:
		break
print(sum_value)


while True:
	fruit = input("请输入你喜欢的水果，输入quit则会退出程序：")
	if fruit == "quit":
		break
	else:
		print("很好，你喜欢这个水果：",fruit)