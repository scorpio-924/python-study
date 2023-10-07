import os
import shutil

dir = r"D:\.aa-刘天天的文件夹\刘天天\蚂蚁python\蚂蚁学python\02-python编程练习100题\第17章\arrange_dir"

for file in os.listdir(dir):
    ext = os.path.splitext(file)[1]
    ext = ext[1:]
    if not os.path.isdir(f"{dir}/{ext}"):
        os.mkdir(f"{dir}/{ext}")

    source_path = f"{dir}/{file}"
    target_path = f"{dir}/{ext}/{file}"
    shutil.move(source_path, target_path)
