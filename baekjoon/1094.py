import sys
input = sys.stdin.readline

n = int(input())
arr = [64]

while True:
  count = sum(arr)
  if count == n:
    print(len(arr))
    break

  if count > n:
    tmp = arr[-1] // 2
    if count - tmp >= n:
      arr.pop()
      arr.append(tmp)
    else:
      arr.pop()
      arr.append(tmp)
      arr.append(tmp)
