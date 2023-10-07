import json
d = {"employees":[{"firstName":"John","lastName":"Doe"},
				 {"firstName":"Anna","lastName":"Smith"},
				 {"firstName":"Peter","lastName":"Jones"}],
	"owners":[{"firstName":"Jack","lastName":"Petter"},
	          {"firstName":"Jessy","lastName":"Petter"}]}

with open("p060.json","w") as f:
	f.write(json.dumps(d,indent=2))