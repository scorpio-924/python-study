content = """
白日依19989881888山尽，黄河入45645546468798978海流.
欲穷12345千里目，更上15619292345一层楼。
"""
import re

pattern = r"(1\d)\d{7}(\d{2})"

print(re.sub(pattern,r"\1******\2",content))