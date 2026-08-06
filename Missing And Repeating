class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        expected_sum = n * (n + 1) // 2
        expected_sq_sum = n * (n + 1) * (2 * n + 1) // 6
        
        actual_sum = sum(arr)
        actual_sq_sum = sum(x * x for x in arr)
        
        # actual_sum - expected_sum = repeating - missing
        sum_diff = actual_sum - expected_sum
        
        # actual_sq_sum - expected_sq_sum = repeating^2 - missing^2
        #                                 = (repeating - missing)(repeating + missing)
        sq_diff = actual_sq_sum - expected_sq_sum
        sum_total = sq_diff // sum_diff  # repeating + missing
        
        repeating = (sum_diff + sum_total) // 2
        missing = repeating - sum_diff
        
        return [repeating, missing]
