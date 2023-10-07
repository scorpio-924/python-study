
import os
print("文件路径是否存在.txt:", os.path.exists("文件路径是否存在.txt"))

print("测试路径.txt:", os.path.exists("文件路径是否存在/测试路径.txt"))

file = r"/零基础入门学python/第10章/文件路径是否存在.txt"

print(f"{file}:",os.path.exists(file))

print("xxx.txt:",os.path.exists("xxx.txt"))