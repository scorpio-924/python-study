with open("写出100个数字.txt", "w", encoding="utf8") as f:
    for number in range(100):
        f.write(str(number) + "\n")