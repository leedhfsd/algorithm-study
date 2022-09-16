s = input()
char = set([])
for i in range(0, len(s)):
  char.add(s[i])
  tmp = s[i]
  for j in range(i+1, len(s)):
    tmp = tmp + s[j]
    char.add(tmp)
    
print(len(char))
