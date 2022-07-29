import sys
input = sys.stdin.readline

s = input().rstrip()

change_one = s.split("0")
change_zero = s. split("1")
res_one, res_zero = 0, 0

for i in range(len(change_one)):
  if change_one[i] != "":
    res_one += 1

for j in range(len(change_zero)):
  if change_zero[j] != "":
    res_zero += 1

if res_one > res_zero:
  print(res_zero)
else:
  print(res_one)
