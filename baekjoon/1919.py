from collections import defaultdict
a = input()
b = input()
dic_a = defaultdict(int)
dic_b = defaultdict(int)
used = set([])
ans = 0 
for char in a:
  dic_a[char] += 1
for char in b:
  dic_b[char] += 1
for char in dic_a.keys():
  ans += abs(dic_a[char] - dic_b[char])
  used.add(char)
for char in dic_b.keys():
  if char not in used:
    ans += abs(dic_a[char] - dic_b[char])

print(ans)

a = input()
b = input()
cnt = [0] * 26
for char in a:
  cnt[ord(char)-ord("a")] += 1
for char in b:
  cnt[ord(char)-ord("a")] -= 1
print(sum(map(abs,cnt)))
