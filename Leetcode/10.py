#https://leetcode.com/problems/container-with-most-water/submissions/
class Solution:
    def maxArea(self, height: List[int]) -> int:
      ans = 0
      left, right = 0, len(height)-1
      while left < right:
        limit = min(height[left], height[right])
        tmp = limit * (right - left)
        if ans < tmp:
          ans = tmp
        if height[left] == limit:
          left += 1
        elif height[right] == limit:
          right -= 1
      return ans
