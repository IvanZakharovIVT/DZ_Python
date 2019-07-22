from datetime import datetime

def timerT(func):
	def abc(*args, **kwargs):
		start = datetime.now()
		result = func(*args, **kwargs);
		print(result)
		endT = datetime.now() - start
		print("Время работы:")
		print(endT)
		return result
	return abc

@timerT
def prog(n):
	res = 0
	y = ((0 - 1000)**3)/3 - (0 * 20)**2
	b = 0
	l = [i for i in range(n)]
	for x in l:
		y1 = ((x - 1000)**3)/3 - (x * 20)**2 + x
		if y1 < y and b == 0:
			b = 1
			res += x - 1
		if y1 > y and b == 1:
			b = 0
			res += x - 1
		y = y1
	return res
ac = prog(20000)