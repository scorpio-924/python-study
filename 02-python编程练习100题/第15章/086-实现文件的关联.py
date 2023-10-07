grade_dict = {}
with open("p086_grade.txt",encoding="utf8") as f:
	for line in f:
		sno,grade = line.strip().split(",")
		grade_dict[sno] = grade
fout = open("p086.txt","w",encoding="utf8")
with open("p086_student.txt",encoding="utf8") as f:
	for line in f:
		sno,sname = line.strip().split(",")
		grade = grade_dict[sno]
		fout.write(f"{sno},{sname},{grade}\n")
fout.close()