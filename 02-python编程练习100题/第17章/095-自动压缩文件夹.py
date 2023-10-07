import os
import zipfile

def do_zip_compress(dirpath):
    output_name = f"{dirpath}.zip"
    parent_name = os.path.dirname(dirpath)
    zip = zipfile.ZipFile(output_name,"w",zipfile.ZIP_DEFLATED)
    for root,dirs,files in os.walk(dirpath):
        for file in files:
            if str(file).startswith("~$"):
                continue
            filepath = os.path.join(root,file)
            writepath = os.path.relpath(filepath,parent_name)
            zip.write(filepath,writepath)
    zip.close()

dirpath = r"D:\.aa-刘天天的文件夹\刘天天\蚂蚁python\蚂蚁学python\02-python编程练习100题\第17章\arrange_dir"
do_zip_compress(dirpath)