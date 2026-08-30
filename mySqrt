class Solution(object):
    def mySqrt(self, x):

        if x < 2:
            return x
        
        low, high = 1, x // 2
        ans = 1
        
        while low <= high:
            mid = low + (high - low) // 2
            sq = mid * mid
            if sq == x:
                return mid
            elif sq < x:
                ans = mid       # mid is a valid candidate (floor so far)
                low = mid + 1
            else:
                high = mid - 1
        
        return ans
