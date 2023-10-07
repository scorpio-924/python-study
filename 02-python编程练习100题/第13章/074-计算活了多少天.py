import datetime

birthday = input("请输入生日：")
birthday_date = datetime.datetime.strptime(birthday,"%Y-%m-%d")

curr_datetime = datetime.datetime.now()

minus_datetime = curr_datetime - birthday_date

print(minus_datetime.days," 天")

print(minus_datetime.days/365)

import datetime

birthday = input("请输入结婚日期：")
birthday_date = datetime.datetime.strptime(birthday,"%Y-%m-%d")

curr_datetime = datetime.datetime.now()

minus_datetime = curr_datetime - birthday_date

print(f"你们已经结婚 {minus_datetime.days} 天")

