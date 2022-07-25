import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))

ans = 0

def dfs(cur, prev, res):
  global ans 
  if cur == n:
    ans = max(ans, res)
    return res

  for i in range(0, n):
    if not visited[i]:
      diff = abs(prev - number[i])
      visited[i] = 1
      dfs(cur+1, number[i], res+diff)
      visited[i] = 0
  
for i in range(n):
  visited = [0 for _ in range(n)]
  visited[i] = 1
  dfs(1, number[i], 0)
print(ans)
