#왼쪽부터 시작해서 자기보다 큰 타워가 있으면 반환 아니면 전부 다 pop하고 0

n = int(input())
height = list(map(int,input().split()))
stack = []
answer = []
for i in range(n):
  while stack:
    if stack[-1][1] > height[i]:
      answer.append(stack[-1][0]+1)
      break
    else:
      stack.pop()
  if not stack:
    answer.append(0)
  stack.append([i, height[i]])

print(" ".join(map(str,answer)))
