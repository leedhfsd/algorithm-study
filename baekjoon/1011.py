import math
tc = int(input())
for _ in range(tc):
	start, end =  map(int,input().split())
	diff = end - start
	tmp = math.sqrt(diff)
	num = int(tmp)
	if num * num == diff:
		print(2 * num - 1)
		continue
	else:
		if diff <= num * num + num:
			print(2 * num)
		else:
			print(2 * num + 1)
