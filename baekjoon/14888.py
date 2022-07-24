#음수 나눗셈하는 경우 // 연산이랑 int(/) 연산이랑 다른 결과 출력됨.
import sys
input = sys.stdin.readline

n = int(input())
number = list(map(int,input().split()))
oper = list(map(int,input().split()))
max_ans = -sys.maxsize
min_ans = sys.maxsize

def dfs(cur, res):
  global max_ans, min_ans
  if cur == n-1:
    max_ans = max(max_ans, res)
    min_ans = min(min_ans, res)
    return 0
  tmp = res
  for i in range(4):
    if oper[i] > 0:
      if i == 0:
        res = res + number[cur+1]
      elif i == 1:
        res = res - number[cur+1]
      elif i == 2:
        res = res * number[cur+1]
      else:
        res = int(res / number[cur+1])
      oper[i] = oper[i] - 1
      dfs(cur+1, res)
      res = tmp
      oper[i] = oper[i] + 1 

dfs(0, number[0])
print(max_ans)
print(min_ans)
