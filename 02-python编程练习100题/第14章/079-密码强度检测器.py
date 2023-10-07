while True:
	pwd = input("请输入密码：")
	have_number = any([i.isdigit() for i in pwd])
	have_upper = any([i.isupper() for i in pwd])

	if have_number and have_upper and len(pwd) >= 6:
		print("密码校验通过")
		break
	else:
		print("密码校验不通过，请重新输入")