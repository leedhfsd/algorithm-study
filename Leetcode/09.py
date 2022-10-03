#https://leetcode.com/problems/3sum/submissions/
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      answer = []
      nums = sorted(nums)
      for i in range(0, len(nums)-1):
        if nums[i] == nums[i-1] and i>0:
          continue
        left, right = i+1, len(nums)-1
        while left < right:
          res = nums[i] + nums[left] + nums[right]
          if res == 0:
            tmp = [nums[i], nums[left], nums[right]]
            if tmp not in answer:
              answer.append(tmp)
            while left < right and nums[left] == nums[left+1]:
              left += 1
            while left < right and nums[right] == nums[right-1]:
              right -= 1
            left, right = left+1, right-1
          elif res > 0:
            right -= 1
          elif res < 0:
            left += 1        
      return answer
