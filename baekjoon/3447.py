import sys
import re

text = sys.stdin.readlines()
ans = ""
for line in text:
	tmp = line
	while True:
		tmp = re.sub("BUG","",tmp)
		if "BUG" not in tmp:
			break
	
	ans += tmp
print(ans[:-1])
