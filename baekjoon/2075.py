#메모리 제약이 있는 문제라 힙의 크기를 제한시키고 push, pop
import sys
import heapq
input = sys.stdin.readline

heap = []

n = int(input())
for i in range(n):
  tmp = list(map(int,input().split()))
  for j in range(len(tmp)):
    if len(heap) < n:
      heapq.heappush(heap, tmp[j])
    else:
      if heap[0] < tmp[j]:
        heapq.heappop(heap)
        heapq.heappush(heap, tmp[j])

print(heap[0])
