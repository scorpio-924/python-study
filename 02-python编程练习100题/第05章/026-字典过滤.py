d = {'a': 1, 'b': 2, 'c': 3}
d = {key:value for key,value in d.items() if value <=1}
print(d)

d = {key:value*90 for key,value in d.items() if value <=1}
print(d)