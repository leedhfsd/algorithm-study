from collections import Counter
from collections import deque
word = input()

res = Counter(word)
left = deque([])
center = deque([])
right = deque([])

for i in sorted(res.keys()):
	if res[i] % 2 == 0:
		tmp = res[i] // 2
		left.append(i*tmp)
		right.appendleft(i*tmp)
	elif res[i] % 2 != 0:
		tmp = res[i] // 2
		left.append(i*tmp)
		right.appendleft(i*tmp)
		center.append(i)

tmp = left+center+right
if "".join(tmp) != "".join(reversed(tmp)):
	print("I'm Sorry Hansoo")
else:
	ans = "".join(tmp)
	print(ans)
