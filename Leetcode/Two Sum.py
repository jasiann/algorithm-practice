class Solution(object):
    def twoSum(self, nums, target):
        seen = {}
        
        for index,num in enumerate(nums):
            new_num = target - num 

            if new_num in seen: 
                return [seen[new_num], index]
            else: 
                seen[num] = index 


        
        
