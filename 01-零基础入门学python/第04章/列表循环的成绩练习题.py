"""
怎样计算成绩的前三名
* 新建一个列表grades，里面的值是 [ 77,88,73,99,82,89,95,86,93 ]
* 将列表grades降序排序
* 输出成绩的最高分、最低分、平均分
* 提取grades的最高分前3名，打印结果
"""
grades = [77,88,73,99,82,89,95,86,93]
grades.sort(reverse=True)

print("最高分",max(grades))
print("最低分",min(grades))
print("平均分",sum(grades)/len(grades))



print("前三名成绩：")
for grade in grades[:3]:
    print(grade)


