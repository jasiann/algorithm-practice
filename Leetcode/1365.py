#Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. 
#That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        ournum = {}
        final = []
        sorted_array = sorted(nums)
        for num, value in enumerate(sorted_array): 
            if value not in ournum: 
                ournum[value] = num

        for num in nums :
            final.append(ournum[num])
        return final 
