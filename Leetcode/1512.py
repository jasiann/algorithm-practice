#Given an array of integers nums, return the number of good pairs.
#A pair (i, j) is called good if nums[i] == nums[j] and i < j.

class Solution(object):
    def numIdenticalPairs(self, nums):
        counting = {} 
        final = 0 
        for num in nums: 
            if num in counting:
                final += counting[num] 
                counting[num] += 1

            else:
                counting[num] = 1 
        return final
