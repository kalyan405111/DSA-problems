class Solution(object):
    def missingNumber(self, nums):
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result

        
