import re
tc = int(input())
s,e = input().split("*")
p = re.compile(s+".*"+e)

for _ in range(tc):
	if p.fullmatch(input()):
		print("DA")
	else:
		print("NE")
