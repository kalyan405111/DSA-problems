class Solution(object):
    def singleNumber(self, nums):
        xor_all = 0
        for num in nums:
            xor_all ^= num
        
        # get the lowest set bit (a bit where x and y differ)
        diff_bit = xor_all & (-xor_all)
        
        x = 0
        for num in nums:
            if num & diff_bit:
                x ^= num
        
        y = xor_all ^ x
        return [x, y]
