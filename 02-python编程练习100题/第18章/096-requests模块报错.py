import requests

r = requests.get("http://antpython.net/")
print(r.text[:100])