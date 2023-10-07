grade = 70
print("是否及格",grade >= 60)
print("是否不及格",grade <= 60)
print("是否满分",grade == 100)
print("是否不是满分",grade != 100)
print("是否属于中等成绩",grade >= 70 and  grade < 90 )
print("是否成绩很顺口",grade in [66,88,99] )
print("判断成绩及格并且以0结尾",grade >= 60 and grade in [60,70,80,90,100] )
