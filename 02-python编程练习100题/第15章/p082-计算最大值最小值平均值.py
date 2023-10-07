def compute_score():
	scores = []
	with open("./p082.txt",encoding="utf8") as fin:
		for line in fin:
			line = line.strip()
			fields = line.split(",")
			scores.append(int(fields[-1]))
	max_score = max(scores)
	min_score = min(scores)
	avg_score = round(sum(scores)/len(scores),2)
	return max_score,min_score,avg_score

max_score,min_score,avg_score = compute_score()
print(max_score,min_score,avg_score)