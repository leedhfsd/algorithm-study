import sys
input = sys.stdin.readline

n = int(input())
inp = list(map(int,input().split()))
budget = int(input())
inp.sort()
ans = -sys.maxsize

for i in range(n):
  if (n-i) * inp[i] <= budget:
    budget -= inp[i]
    if ans < inp[i]:
      ans = inp[i]
  else:
    res = budget // (n-i)
    if ans <= res:
      ans = res
      break

print(ans)
