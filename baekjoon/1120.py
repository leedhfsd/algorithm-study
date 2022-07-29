import sys
input = sys.stdin.readline

a, b = input().rstrip().split()
diff = len(b) - len(a)
word_set = set()
ans = sys.maxsize

def check(a, b): 
  res = 0
  for i in range(len(b)):
    if a[i] == "*":
      continue
    elif a[i] != b[i]:
      res += 1
  return res

def solution(inp, remain):
  global ans, b
  if remain == 0:
    ans = min(ans, check(inp, b))
    return 0

  left = "*" + inp
  right = inp + "*"

  if left not in word_set:
    solution(left, remain-1)
  
  if right not in word_set:
    solution(right, remain-1)

  word_set.add(left)
  word_set.add(right)

if len(a) == len(b):
  ans = check(a,b)
else:
  solution(a, diff)

print(ans)
