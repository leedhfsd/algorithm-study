import sys
input = sys.stdin.readline

n = int(input())
switch = ["*"] + list(map(int,input().split()))
tc = int(input())


def change(idx):
  global switch
  if idx >= 1 and idx <= n:
    if switch[idx] == 0:
      switch[idx] = 1
    elif switch[idx] == 1:
      switch[idx] = 0

for _ in range(tc):
  sex, number = map(int, input().split())
  if sex == 1:
    for i in range(number, n+1, number):
      change(i)
  
  if sex == 2:
    if number == 1 or number == n:
      change(number)
    elif 1 < number < n:
      left, right = number-1, number+1
      if switch[left] != switch[right]:
        change(number)
      else:
        while left-1 >= 1 and right+1 <= n:
          if switch[left-1] == switch[right+1]:
            left -= 1
            right += 1
          else:
            break
        for i in range(left, right+1):
          change(i)

for i in range(1, len(switch)):
  print(switch[i], end=" ")
  if i % 20 == 0:
    print()
