import sys
import heapq
input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
  inp = int(input().rstrip())
  if inp != 0:
    heapq.heappush(heap, [abs(inp), inp])
  else:
    if not heap:
      print(0)
    else:
      print(heapq.heappop(heap)[1])
