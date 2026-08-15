class Solution(object):
    def longestSubsequence(self, nums):
        total = 0
        for num in nums:
            total ^= num
        
        if total != 0:
            return len(nums)
        
        # total XOR is 0 — try removing one non-zero element
        if any(num != 0 for num in nums):
            return len(nums) - 1
        
        return 0
