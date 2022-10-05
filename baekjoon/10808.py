text = input()
dic = dict()
for i in range(26):
  dic[chr(ord("a")+i)] = 0

for char in text:
  dic[char] += 1

print(*dic.values())
