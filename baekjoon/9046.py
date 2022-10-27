tc = int(input())
for _ in range(tc):
	inp = input()
	dic = dict()
	for char in inp:
		if char != " ":
			if char not in dic:
				dic[char] = 1
			else:
				dic[char] += 1
	cnt = list(dic.items())
	cnt.sort(key = lambda x: -x[1])
	if len(cnt) == 1:
		print(cnt[0][0])
	else:
		if cnt[0][1] == cnt[1][1]:
			print("?")
		else:
			print(cnt[0][0])
