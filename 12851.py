# 내 풀이 n에서 k로 간다.
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())

def bfs(start):
	visited = [sys.maxsize for _ in range(200001)]
	dq = deque([(start, 0)])
	dx = [-1,1,2]
	visited[start] = 1
	ans = 0
	while dq:
		x, cnt = dq.popleft()

		if x == m:
			if visited[m] > cnt:
				visited[m] = cnt
				ans = 1
			elif visited[m] == cnt:
				ans += 1
			
		for i in range(3):
			if i == 2:
				nx = x * dx[i]
			else:
				nx = x + dx[i]

			if 0 <= nx <= 100000 and visited[nx] > cnt:
				visited[nx] = cnt+1
				dq.append((nx, cnt+1))
	
	print(visited[m])
	print(ans)

bfs(n)


# 다른 사람 풀이. k에서 n으로 간다
from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N-K)
    print(1)

else:
    visited = [False] * 100001
    ans = 100001
    amount = 0
    q = deque()
    q.append((K, 0))
    while q:
        pos, cnt = q.popleft()
        visited[pos] = True

        if cnt > ans:
            continue

        if pos == N:
            if cnt < ans:
                ans = cnt
                amount = 1
            elif cnt == ans:
                amount += 1
        
        else:
            if not pos % 2 and not visited[pos % 2]:
                q.append((pos // 2, cnt + 1))
            if 0 <= pos - 1 and not visited[pos-1]:
                q.append((pos - 1, cnt + 1))
            if pos + 1 <= 100000 and not visited[pos+1]:
                q.append((pos + 1, cnt + 1))

    print(ans)
    print(amount)
