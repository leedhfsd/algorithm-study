import sys
input = sys.stdin.readline

a, p = map(int,input().split())
cand = [a]
idx = 0

while True:
  res = 0
  tmp = list(str(a))
  for i in range(len(tmp)):
    res +=  pow(int(tmp[i]), p)
  a = res
  if a in cand:
    idx = cand.index(a)
    break
  cand.append(a)
  
print(len(cand[:idx]))
