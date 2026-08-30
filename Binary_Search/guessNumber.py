class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n
        
        while low <= high:
            mid = (low + high) // 2
            result = guess(mid)
            
            if result == 0:
                return mid
            elif result == -1:   # mid is too high, pick is lower
                high = mid - 1
            else:                # result == 1, mid is too low, pick is higher
                low = mid + 1
        
        return -1  # shouldn't happen since a valid answer always exists
