def compute(x,y,method="add"):
    if method == "add":
        print(f"{x}+{y}=",x+y)
    elif method == "sub":
        print(f"{x}-{y}=", x - y)
    elif method == "mul":
        print(f"{x}*{y}=", x * y)
    elif method == "div":
        print(f"{x}/{y}=", x / y)


compute(3,4,"add")
compute(3,method="sub",y=4,)
compute(x=3,y=4,method="sub")