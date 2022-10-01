#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
#https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 0
        for i in range(0, len(nums)-1):
            if nums[i] > nums[i+1]:
                res = i+1
                break
        
        return nums[res]
