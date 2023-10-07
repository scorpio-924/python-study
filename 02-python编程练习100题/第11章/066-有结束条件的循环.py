
#老师的代码
import time

i = 0
while True:
	i = i + 1
	print("hello")
	if i > 3:
		print("end of loop")
		break
	time.sleep(i)


#我自创的代码
import time

i = 0

for i in range(1,5):
    i = i + 1
    print("hello")
    time.sleep(i)
print("end of loop")
