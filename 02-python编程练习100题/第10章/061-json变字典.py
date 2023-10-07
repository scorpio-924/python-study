import json
import pprint
with open("p060.json") as f:
	d = json.loads(f.read())
pprint.pprint(d)