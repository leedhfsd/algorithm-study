import sys
input = sys.stdin.readline
grade = {}
tc, num = map(int,input().split())
inp = []
for _ in range(tc):
  inp.append(list(map(int,input().split())))

inp.sort(key = lambda x: (-x[1], -x[2], -x[3]))
res = 1
idx = 0
for i in range(len(inp)):
  if inp[i][0] == num:
    idx = i
    break

for i in range(len(inp)):
  if inp[i][1:] == inp[idx][1:]:
    print(res)
    break
  else:
    res += 1
