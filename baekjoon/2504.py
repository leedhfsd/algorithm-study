import sys
input = sys.stdin.readline

inp = input().rstrip()
stack = []
tmp = 1
ans = 0

for i in range(len(inp)):
  if inp[i] == "(":
    stack.append(inp[i])
    tmp *= 2
  elif inp[i] == "[":
    stack.append(inp[i])
    tmp *= 3
  elif inp[i] == ")":
    if not stack or stack[-1] == "[":
      ans = 0
      break
    if inp[i-1] == "(":
      ans += tmp
    tmp = tmp // 2
    stack.pop()
  elif inp[i] == "]":
    if not stack or stack[-1] == "(":
      ans = 0
      break
    if inp[i-1] == "[":
      ans += tmp
    tmp = tmp // 3
    stack.pop()

if stack:
  ans = 0
print(ans)
