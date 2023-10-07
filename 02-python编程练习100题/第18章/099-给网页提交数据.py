import requests

url = "http://antpython.net/webspider/grade_form"
params = {
    "sname":"蚂蚁099",
    "yuwen":88,
    "shxue":99,
    "yingyu":66,
}

resp = requests.post(url,data=params)
print(resp.status_code)