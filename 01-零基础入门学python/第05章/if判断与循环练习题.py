numbers = [2,3,5,8,7,4,1,6]
target = 8
result = []
for a in numbers:
    for b in numbers:
        # print(a,b)
        if a + b == target and (a,b) not in result:
            print(f"找到了一对数字:{a}+{b}=={target}")
            result.append((a,b))
            result.append((b, a))
