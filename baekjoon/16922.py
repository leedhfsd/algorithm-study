import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

number = set([])
inp = [1, 5, 10, 50]
n = int(input())

def recursion(cnt, res, idx):
  if cnt == n:
    number.add(res)
    return 0

  for i in range(idx, 4):
    recursion(cnt+1, res+inp[i], i)

recursion(0,0,0)
print(len(number))
