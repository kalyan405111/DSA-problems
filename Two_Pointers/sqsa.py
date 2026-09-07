class Solution(object):
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n

        left = 0
        right = n - 1
        position = n - 1

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[position] = nums[left] * nums[left]
                left += 1
            else:
                result[position] = nums[right] * nums[right]
                right -= 1
            position -= 1  # now runs every iteration
        return result