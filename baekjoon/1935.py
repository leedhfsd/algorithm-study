import sys
input = sys.stdin.readline

n = int(input())
inp = input().rstrip()

stack = []
idx = ord("A")
number = {}
for i in range(n):
  number[chr(idx)] = int(input())
  idx += 1

for i in range(len(inp)):
  if inp[i] not in "*+/-":
    stack.append(number[inp[i]])
  else:
    a = stack.pop()
    b = stack.pop()
    if inp[i] == "+":
      stack.append(a+b)
    elif inp[i] == "*":
      stack.append(a*b)
    elif inp[i] == "-":
      stack.append(b-a)
    elif inp[i] == "/":
      stack.append(b/a)

print("%.2f"%stack[-1])
