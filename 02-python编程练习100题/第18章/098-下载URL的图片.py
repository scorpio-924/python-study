import requests

url = "http://antpython.net/static/pubdatas/webspider/goodimgs/9.jpeg"
r = requests.get(url)

with open("p098.jpeg","wb") as f:
	f.write(r.content)