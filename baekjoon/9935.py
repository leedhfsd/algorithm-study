#replace으로 하면 시간초과 뜸. 들어오는 문자가 target의 마지막 문자라면 target이 있는지 확인 후 pop

import sys
input = sys.stdin.readline

inp = input().rstrip()
target = input().rstrip()
stack = []

for i in range(len(inp)):
  stack.append(inp[i])
  if inp[i] == target[-1]:
    if "".join(stack[-len(target):]) == target:
      cnt = len(target)
      while cnt > 0:
        stack.pop()
        cnt -= 1

if len(stack) == 0 : print("FRULA")
else: print(''.join(stack))
