#내 풀이
import sys
input = sys.stdin.readline
n = int(input())

level3 = [[' ', ' ', '*', ' ', ' '], [' ', '*', ' ', '*', ' '], ['*', '*', '*', '*', '*']]

def solution(n):
  if n == 3:
    return level3
  
  ans = [[" " for _ in range(2*n-1)] for _ in range(n)]
  
  base = solution(n//2)
  for i in range(n):
    if i < n//2:
      ans[i] = [" "]*(n//2) + base[i] + [" "]*(n//2)
    else:
      ans[i] = base[i-n] + [" "] + base[i-n]
  
  return ans

ans = solution(n)
for line in ans:
  print("".join(line))
# 다른 사람 풀이

import sys
input = sys.stdin.readline
n = int(input())

def sol(n):
  if n == 3:
    return ["  *  "," * * ","*****"]
  
  prev = sol(n//2)
  half = n // 2
  return [" "*half + i + " "*half for i in prev] + [i + " " + i for i in prev]

print("\n".join(sol(n)))
  
