#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
#https://leetcode.com/problems/maximum-product-subarray/
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        tmp_max = tmp_min = res = nums[0]
        for num in nums[1:]:
            tmp = tmp_max
            tmp_max = max(tmp_max * num, tmp_min * num, num)
            tmp_min = min(tmp * num, tmp_min * num, num)
            res = max(tmp_max, tmp_min, res)
    
        return res
