#https://leetcode.com/problems/climbing-stairs/submissions/#
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for _ in range(46)]
        dp[1], dp[2] = 1, 2
        if n <= 2:
          return n
        else:
          for i in range(3, n+1):
            dp[i] = dp[i-2] + dp[i-1]
          return dp[n]
