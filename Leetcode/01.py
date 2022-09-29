#https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions 75제
#https://leetcode.com/problems/two-sum/
  
def twoSum(nums, target):
    hash_table = {}
    for idx, val in enumerate(nums):
        hash_table[val] = idx 
    
    for idx, val in enumerate(nums):
        if target-val in hash_table and idx != hash_table[target-val]:
            return [idx, hash_table[target-val]]
