#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
#https://leetcode.com/problems/product-of-array-except-self/submissions/
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []
        res = 1
        for i in range(0, len(nums)):
            ans.append(res)
            res = res * nums[i]
        res = 1
        for i in range(len(nums)-1,-1,-1):
            ans[i] = ans[i] * res
            res = res * nums[i]
        
        return ans
            
