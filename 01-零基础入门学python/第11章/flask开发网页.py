from flask import Flask
app = Flask("我的网页")

@app.route("/myflask")
def hello():
    return"哈哈哈哈,第一次做网页"
app.run()