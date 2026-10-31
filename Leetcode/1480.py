#Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
#Return the running sum of nums.

class Solution(object):
    def runningSum(self, nums):
        running_sum = 0 
        final = []

        for num in nums: 
            running_sum+= num
            final.append(running_sum)
        return final
