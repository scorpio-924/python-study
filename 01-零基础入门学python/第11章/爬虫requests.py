import requests

URL = "http://www.baidu.com"

r = requests.get(URL)

print(r.status_code)
print(r.text)