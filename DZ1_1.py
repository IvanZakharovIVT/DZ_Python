for x in range(100):
	if x%15 == 0:
		print("FuzzBuzz")
	elif x%3 == 0:
		print("Fuzz")
	elif x%5 == 0:
		print("Buzz")
	else:
		print(x)