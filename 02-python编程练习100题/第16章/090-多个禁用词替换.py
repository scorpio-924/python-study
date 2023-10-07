content = """
这个商品很好，质量最好、用起来很不错，并且价格最低，绝对物美价廉
"""

import re

pattern = r"最好|最低|绝对"

print(re.sub(pattern,"***",content))