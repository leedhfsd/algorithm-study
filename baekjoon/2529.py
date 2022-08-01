import sys
input = sys.stdin.readline

visited = [0 for _ in range(10)]
n = int(input())
oper = input().rstrip().split()
res_max = -sys.maxsize
res_min = sys.maxsize

def solution(cur, idx, res):
  global res_max, res_min
  if idx == n:
    number = int(res)
    if number > res_max:
      res_max = number
    if number < res_min:
      res_min = number
    return res

  op = oper[idx]
  for i in range(len(visited)):
    if visited[i]: continue
    if op == ">":
      if cur > i:
        visited[i] = 1
        solution(i, idx+1, res+str(i))
        visited[i] = 0
    elif op == "<":
      if cur < i:
        visited[i] = 1
        solution(i, idx+1, res+str(i))
        visited[i] = 0

for i in range(len(visited)):
  visited[i] = 1
  solution(i, 0, str(i))
  visited[i] = 0


print(res_max)
if len(str(res_min)) < n+1:
  print("0" + str(res_min))
else:
  print(res_min)
