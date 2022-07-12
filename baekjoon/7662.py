# 최대힙과 최소힙을 따로 만들고 index로 동기화 하기.
import sys
import heapq
input = sys.stdin.readline

for i in range(int(input())):
  visited = [False] * 1000001
  minHeap, maxHeap = [],[]
  for j in range(int(input())):
    inst, num = input().split()
    if inst == "I":
      heapq.heappush(minHeap, (int(num), j))
      heapq.heappush(maxHeap, (-int(num), j))
      visited[j] = True
    elif num == "1":
      while maxHeap and not visited[maxHeap[0][1]]:
        heapq.heappop(maxHeap)
      if maxHeap:
        visited[maxHeap[0][1]] = False
        heapq.heappop(maxHeap)
    elif num == "-1":
      while minHeap and not visited[minHeap[0][1]]:
        heapq.heappop(minHeap)
      if minHeap:
        visited[minHeap[0][1]] = False
        heapq.heappop(minHeap)
  while minHeap and not visited[minHeap[0][1]]:
    heapq.heappop(minHeap)
  while maxHeap and not visited[maxHeap[0][1]]:
    heapq.heappop(maxHeap)
  if not minHeap or not maxHeap:
    print("EMPTY")
  else:
    print(-maxHeap[0][0], minHeap[0][0])      


