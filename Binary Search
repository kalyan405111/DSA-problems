class Solution(object):
    def search(self, nums, target):
       
       def binary(nums, low, high):
        if low >high:
            return -1
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return binary(nums, mid+1, high)
        else :
            return binary(nums, low, mid-1)
       return binary(nums, 0, len(nums)-1)
    
