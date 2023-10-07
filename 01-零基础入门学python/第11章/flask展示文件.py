
from flask import Flask

app = Flask("英语词典访问")

@app.route("/english")
def show_file():
    with open("英汉翻译.txt", encoding="utf8") as f:
        cont = f.read()
        cont = cont.replace("\n","<br/>")
        return cont
app.run()