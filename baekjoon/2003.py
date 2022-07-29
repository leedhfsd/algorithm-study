import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = list(map(int,input().split()))
count = 0
left = 0
right = 1
res = arr[left]

while True:
  if res >= m:
    if res == m:
      count += 1
    res -= arr[left]
    left += 1
  elif right == n:
    break
  elif res < m:
    res += arr[right]
    right += 1

print(count)


  
