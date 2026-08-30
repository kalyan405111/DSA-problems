class Solution(object):
    def lower(self, nums, target):
        n = len(nums)
        lb = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                lb = mid
                high = mid - 1   # keep searching left for first occurrence
        return lb

    def upper(self, nums, target):
        n = len(nums)
        ub = -1
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                ub = mid
                low = mid + 1    # keep searching right for last occurrence
        return ub

    def searchRange(self, nums, target):
        lb = self.lower(nums, target)
        if lb == -1:
            return [-1, -1]
        ub = self.upper(nums, target)
        return [lb, ub]
