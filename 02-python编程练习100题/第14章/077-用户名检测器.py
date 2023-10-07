while True:
	username = input("请输入用户名：")
	with open("p077_users.txt") as f:
		users = [name.strip() for name in f.readlines()]

	if len(username) < 6:
		print("长度小于6位，请重新输入")
		continue

	if username in users:
		print("用户名已存在，请重新输入")
		continue
	else:
		print("用户名检测通过")
		break