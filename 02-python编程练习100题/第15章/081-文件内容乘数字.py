with open("p081.txt") as fin, open("p081_output.txt", "w") as fout:
    for line in fin:
        if "x,y" in line:
            fout.write(line)
        else:
            [x, y] = line.strip().split(",")
            x = int(x) * 2
            y = int(y) * 2
            fout.write(f"{x},{y}\n")
