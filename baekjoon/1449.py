import sys
input = sys.stdin.readline

n, stk = map(int,input().split())
inp = list(map(int,input().split()))
inp.sort()
loc = []
for i in range(len(inp)):
  for j in [inp[i] - 0.5, inp[i], inp[i] + 0.5]:
    if j not in loc:
      loc.append(j)
  
left, right = 0, 0
res = 0
while right <= len(loc)-1:
  if loc[right] - loc[left] < stk:
    right += 1
  else:
    res += 1
    right += 1
    left = right

if right - left > 0:
  res += 1
  print(res)
else:
  print(res)
