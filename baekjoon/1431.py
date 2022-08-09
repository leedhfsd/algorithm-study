import sys
input = sys.stdin.readline

tc = int(input())
serial = []
for _ in range(tc):
  serial.append(input().rstrip())

def sort_by_num(inp):
  res = 0
  for i in inp:
    if i.isdigit():
      res += int(i)
  return res
    
serial.sort(key = lambda x: (len(x), sort_by_num(x),x))
for i in serial:
  print(i)
