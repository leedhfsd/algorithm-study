n = int(input())
for _ in range(n):
  a, b = input().split()
  if sorted(a) == sorted(b):
    print("Possible")
  else:
    print("Impossible")
