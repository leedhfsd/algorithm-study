import sys
input = sys.stdin.readline

h, w = map(int,input().split())
n = int(input())
stk = []
for _ in range(n):
  r, c = map(int,input().split())
  stk.append((r,c))

res = 0

for i in range(len(stk)):
  a, b = stk[i]
  for j in range(i+1,len(stk)):
    c, d = stk[j]
    flag = False

    if (a+c <= w and max(b,d) <= h) or (b+d <= h and max(a,c) <= w):
      flag = True
    if (a+d <= w and max(b,c) <= h) or (b+c <= h and max(a,d) <= w):
      flag = True
    if (b+c <= w and max(a,d) <= h) or (a+d <= h and max(b,c) <= w):
      flag = True
    if (b+d <= w and max(a,c) <= h) or (a+c <= h and max(b,d) <= w):
      flag = True
    
    if flag:
      tmp = a * b + c * d
      if tmp > res:
        res = tmp
print(res)
