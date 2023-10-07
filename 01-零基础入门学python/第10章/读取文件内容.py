
# f = open("访客列表.txt",encoding='utf8')
# content = f.read()
# print(content)
# f.close()
#
# with open("访客列表.txt",encoding='utf8') as f:
#     content = f.read()
#     print(content)

# with open("访客列表.txt",encoding='utf8') as f:
#     for line in f:
#         # line = line[:-1]
#         line = line.rstrip()
#         print(line,type(line))


with open("访客列表.txt", encoding='utf8') as f:
    lines = f.readlines()
    lines = [x[:-1] for x in lines]
    print(lines)
