#Given an integer array nums, 
#return true if any value appears at least twice in the array, 
#and return false if every element is distinct.

class Solution(object):
    def containsDuplicate(self, nums):
        final = {}
        for num in nums: 
            if num not in final: 
                final[num] = 1
            else:
                return True
        return False
