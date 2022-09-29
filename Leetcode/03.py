#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        tmp = set(nums)
        if len(tmp) != len(nums):
            return True
        else:
            return False
