import requests

r = requests.get("http://antpython.net/static/py100/life_is_great.txt")
print(r.text)