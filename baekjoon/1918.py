import sys
input = sys.stdin.readline

inp = list(input().rstrip())
idx = 0

def postfix(arr):
  res = []
  for i in range(len(arr)):
    if arr[i] in "-+*/":
      res = arr[:i] + arr[i+1:] + arr[i:i+1]
      break
  return "".join(res)

def parenthesis(inp):
  stack = []
  for i in range(len(inp)):
    stack.append(inp[i])
    if inp[i] == ")":
      for j in range(len(stack)):
        if stack[j] == "(":
          idx = j
      res = mul_div(stack[idx+1:-1])
      res = plus_minus(res)
      for _ in range(len(stack)-idx):
        stack.pop()
      stack.append("".join(res))
  return stack

def mul_div(arr):
  stack = []
  for i in range(len(arr)):
    stack.append(arr[i])
    if arr[i-1] == "*" or arr[i-1] == "/":
      res = postfix(stack[-3:])
      for _ in range(3):
        stack.pop()
      stack.append(res)
  return stack

def plus_minus(arr):
  stack = []
  for i in range(len(arr)):
    stack.append(arr[i])
    if arr[i-1] == "+" or arr[i-1] == "-":
      res = postfix(stack[-3:])
      for _ in range(3):
        stack.pop()
      stack.append(res)
  return stack

if ")" in inp:
  inp = parenthesis(inp)
  print(inp)
inp = mul_div(inp)
inp = plus_minus(inp)
print("".join(inp))
