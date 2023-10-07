def compute(x,y,method):
    if method == "add":
        return x + y
    elif method == "sub":
        return x - y
    elif method == "mul":
        return x * y
    elif method == "div":
        return x / y

def add(x,y):
    return compute(x,y,"add")

def sub(x,y):
    return compute(x,y,"sub")
print(add(3,5))
print(sub(5,3))