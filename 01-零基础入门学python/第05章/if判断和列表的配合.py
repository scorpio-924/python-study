numbers = range(10)
for number in numbers:
	if number % 2 == 0:
		print("发现一个偶数",number)
	else:
		print("发现一个奇数",number)
print("数据读取完毕")

fruits = ["apple","pear","orange"]

if fruits:
	for fruit in fruits:
		print("接下来吃这个水果：",fruit)
else:
	print("抱歉，咱没有水果可以吃")

fruits = []

if fruits:
	for fruit in fruits:
		print("接下来吃这个水果：",fruit)
else:
	print("抱歉，咱没有水果可以吃")