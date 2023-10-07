from datetime import datetime

age = int(input("请输入年龄："))
year_birth = datetime.now().year - age
print(f"你的出生年份是：{year_birth}")