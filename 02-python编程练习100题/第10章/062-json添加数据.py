import json
with open("p060.json") as f:
	d = json.loads(f.read())
d["employees"].append({"firstName":"Albert","lastName":"Bert"})

with open("p062.json","w") as f:
	f.write(json.dumps(d,indent=2))