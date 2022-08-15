h, w = map(int,input().split())
water = list(map(int,input().split()))
res = 0
for i in range(1, w-1):
  left = max(water[:i])
  right = max(water[i+1:])

  tmp = min(left, right)
  if water[i] < tmp:
    res += tmp - water[i]

print(res)
