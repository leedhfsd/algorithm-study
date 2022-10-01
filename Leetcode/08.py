#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions
#https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        try: 
            tmp = nums.index(target)
        except:
            tmp = -1
        return tmp
        
