class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k%=n
        result=nums[-k:] + nums[:-k] if k else n[:]
        for i in range(n):
            nums[i]=result[i]
