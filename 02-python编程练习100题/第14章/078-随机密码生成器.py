import string
import random

words = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation

len = int(input("请输入密码位数："))
chosen = random.sample(words,len)
password = "".join(chosen)
print(password)