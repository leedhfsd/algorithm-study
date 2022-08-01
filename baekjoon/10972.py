import sys
input = sys.stdin.readline

n = int(input())
inp = list(map(int,input().split()))
flag = False
for i in range(len(inp)-1, 0, -1):
  if inp[i-1] < inp[i]:
    for j in range(len(inp)-1 , 0, -1):
      if inp[i-1] < inp[j]:
        inp[i-1], inp[j] = inp[j], inp[i-1]
        inp = inp[:i] + sorted(inp[i:]) 
        flag = True
        break
  if flag:
    print(*inp)
    break

if not flag:
  print(-1)
