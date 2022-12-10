def JumpRank(names, marks, updates, n):
	x = [[0 for j in range(3)] for i in range(n)]
	for i in range(n):
		x[i][0] = names[i]
		x[i][1] = marks[i] + updates[i]
		x[i][2] = i + 1
	highest = x[0]
	for j in range(1, n):
		if (x[j][1] >= highest[1]):
			highest = x[j]
	print("Name: ", highest[0], ", Jump: ",abs(highest[2] - 1))
names = ["A","B","C"]
marks = list(map(int,input('Marks of the Students: ').split(',')))
updates = list(map(int,input('Update in the Marks: ').split(',')))
n = len(names)
JumpRank(names,marks,updates,n)
 
