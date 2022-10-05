from collections import defaultdict
n = int(input())
seq = list(map(int,input().split()))
v = int(input())
dic = defaultdict(int)
for num in seq:
  dic[num] += 1

print(dic[v])
