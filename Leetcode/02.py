# https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
# 최대 최소값 비교할때 if문 보다 min max가 더 빠르다 왜?

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = 10000
        res = 0
        for price in prices:
            cheap = min(cheap, price)
            if price - cheap > res:
                res = price - cheap
        return res
