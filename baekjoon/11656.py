import sys
input = sys.stdin.readline

word = []
inp = input().rstrip()
for i in range(len(inp)):
  word.append(inp[i:])
word.sort()
print("\n".join(word))
