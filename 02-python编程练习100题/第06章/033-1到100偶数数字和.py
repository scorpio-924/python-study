sum_value = 0
for i in range(1,101):
	if i % 2 == 1:
		continue
	sum_value += i
print(sum_value)

print(sum([x for x in range(1,101) if x % 2 == 0]))