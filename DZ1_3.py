l = [1, 1, 2, 3, 5, 4, 5, 5, 6]
l1 = []
for x in l:
	if x not in l1:
		l1.append(x)
print(l1)