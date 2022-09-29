#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
#https://leetcode.com/problems/maximum-subarray/submissions/
#최장 부분 수열 문제. maxNumber[i] = max(number[i], number[i] + maxNumber[i-1]);
#즉 이전 값 활용한 것이 더 큰지, 사용하지 않고 스스로가 더 큰지 체크함

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = ans = nums[0]
        for num in nums[1:]:
            res = max(num, res+num)
            ans = max(res, ans)
                
        return ans
