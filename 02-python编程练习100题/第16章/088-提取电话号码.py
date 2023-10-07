
import re
content = """
白日19989881888依山尽，黄河入45645645667889899海流。
欲穷12345千里目，更上15619292345一层楼。
"""

pattern = r"1\d{10}"
results = re.findall(pattern,content)

for result in results:
	print(result)