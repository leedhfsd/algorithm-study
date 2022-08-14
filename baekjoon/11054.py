n = int(input())
arr = list(map(int,input().split()))
r_arr = list(reversed(arr))

inc = [1 for _ in range(n)]
dec = [1 for _ in range(n)]

for i in range(n):
	for j in range(i):
		if arr[j] < arr[i]:
			inc[i] = max(inc[j] + 1, inc[i])
		if r_arr[j] < r_arr[i]:
			dec[i] = max(dec[j] + 1 , dec[i])
ans = 0
dec.reverse()
for i in range(n):
	if ans < inc[i] + dec[i]:
		ans = inc[i] + dec[i]
print(ans-1)
