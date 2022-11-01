import sys
import re
input = sys.stdin.readline
for _ in range(int(input())):
	tc = input().rstrip()
	res = re.fullmatch('(100+1+|01)+', tc)
	if res:
		print("YES")
	else:
		print("NO")
