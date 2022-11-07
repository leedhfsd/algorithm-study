n, m = map(int,input().split())
number = list(input().split())
ans = -1
def bt(cur):
	global ans
	if int(cur) > n:
		return
	else:
		if int(cur) <= n and ans <= int(cur):
			ans = int(cur)
		for num in number:
			tmp = cur + num
			bt(tmp)
def bt_1(res):
	global ans
	if res > n:
		return
	
	if res > ans:
		ans = res
	for num in number:
		res = res * 10 + num
		bt(res)
		res = (res - num) // 10
bt("0")
bt_1(0)
print(ans)
