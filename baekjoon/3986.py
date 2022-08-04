import sys
input = sys.stdin.readline

tc = int(input())
res = 0
for _ in range(tc):
  inp = list(input().rstrip())
  stack = []
  for char in inp:
    if not stack:
      stack.append(char)
      continue
    else:
      if stack[-1] == char:
        stack.pop()
      else:
        stack.append(char)
  
  if not stack:
     res += 1

print(res)
