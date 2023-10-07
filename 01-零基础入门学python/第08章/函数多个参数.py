def introduce(name,gender):
	"""
	幼儿园自我介绍
	"""
	print(f"大家好，我的名字是：{name}，是个小{gender}")
# 需要按照顺序提供参数，顺序不能乱
#这叫做位置实参，按位置提供
introduce("小明","男生")
introduce("小白","女生")
#调用参数时，响应的提供多个参数

#
# 调用函数实现了
# name = "小明",gender = "男生"
# name = "小白",gender = "女生"
#
# 顺序不能乱