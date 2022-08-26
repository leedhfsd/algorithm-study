MD = 1000000007
import math
m = int(input())
res = 0

def recursion(x, n):
  if n == 1:
    return x
  else:
    tmp = recursion(x, n//2) % MD
    if n % 2 == 0:
      return (tmp * tmp) % MD 
    elif n % 2 != 0:
      return (tmp * tmp * x) % MD
  

for _ in range(m):
  a, b = map(int,input().split())
  gc = math.gcd(a, b)
  a = a // gc
  b = b // gc
  res += b * recursion(a, MD-2) % MD
  res %= MD

print(res)
