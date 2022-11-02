import re
p = re.compile('[^a-zA-Z\- ]')
cand = []
while True:
	word = input()
	tmp = re.sub(p,"",word)
	cand.extend(tmp.split())
	if "E-N-D" in word:
		break
print(sorted(cand, key=lambda x: -len(x))[0].lower())
