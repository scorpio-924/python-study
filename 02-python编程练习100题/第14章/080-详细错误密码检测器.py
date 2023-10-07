from typing import List

while True:
	msgs: list[str] = []
	psw = input("请输入密码：")
	if not any([i.isdigit() for i in psw]):
		msgs.append("需要至少一位数字")
	if not any([i.isupper() for i in psw]):
		msgs.append("需要至少一位大写字母")
	if len(psw) < 6:
		msgs.append("需要至少6位密码")
	if len(msgs) == 0:
		print("密码检测通过")
		break
	else:
		print("密码不通过，有如下原因：")
		for note in msgs:
			print("*",note)