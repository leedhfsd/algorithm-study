#https://leetcode.com/problems/coin-change/submissions/
from collections import deque
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0
        visited = set(coins)
        dq = deque([])
        for coin in coins:
          dq.append((coin, 1))
        
        while dq:
          res, cnt = dq.popleft()
          if res == amount:
            return cnt
          for i in range(len(coins)):
            tmp = res + coins[i]
            if tmp not in visited and tmp <= amount:
              visited.add(tmp)
              dq.append((tmp, cnt+1))
        return -1
