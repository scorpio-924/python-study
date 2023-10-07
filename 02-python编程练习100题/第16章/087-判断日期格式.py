import re

def date_is_right(date):
	return re.match("\d{4}-\d{2}-\d{2}",date) is not None

print("2021-05-20",date_is_right("2021-05-20"))
print("202-05-20",date_is_right("202-05-20"))