a = int(input())
b = int(input())
c = int(input())

tmp = str(a * b * c)
res = [0] * 10
for char in tmp:
  res[ord(char)-ord("0")] += 1

for val in res:
  print(val)
