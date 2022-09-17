n, l = map(int,input().split())
res = 0
start = -1
for i in range(l, 101):
  tmp = (i*i-i)/2
  if (n-tmp)%i == 0 and (n-tmp) // i >= 0:
    res = i
    start = (n-tmp)//i
    break

if start == -1:
  print(-1)
else:
  start = int(start)
  for i in range(start, start+res):
    print(i, end=" ")
