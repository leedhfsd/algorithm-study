#regexp
import sys
import re
input = sys.stdin.readline
spec = set(["A","B","C","D","E","F"])
tc = int(input())
p = re.compile('^[A-F]?A+F+C+[A-F]?$')

for _ in range(tc):
	word = input().rstrip()
	res = p.match(word)
	if res == None:
		print("Good")
	else:
		print("Infected!")
