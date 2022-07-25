# 메모리 초과
import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())

def solution(num):
  if num % 30 == 0:
    return num
  
  arr = list(str(num))
  res = list(permutations(arr, len(arr)))
  for i in res:
    new = int("".join(i))
    if len(str(new)) == len(arr):
      if new % 30 == 0:
        return new
  return -1

print(solution(n))

#30으로 나눠질려면 모든 자릿수 더한게 3의 배수 + 마지막 자리가 0
import sys
from itertools import permutations
input = sys.stdin.readline

n = input().rstrip()

def solution(num):
  arr = list(num)
  arr.sort(reverse=True)
  if arr[-1] != "0":
    return -1
  else:
    sum = 0
    for i in range(len(arr)):
      sum += int(arr[i])
    if sum % 3 == 0:
      return "".join(arr)
    else:
      return -1

print(solution(n))
