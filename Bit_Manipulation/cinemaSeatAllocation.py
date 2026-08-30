class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        
        row_masks = defaultdict(int)
        for row, seat in reservedSeats:
            if 2 <= seat <= 9:
                bit = seat - 2
                row_masks[row] |= (1 << bit)
        
        LEFT = 0b00001111   # seats 2,3,4,5
        MID  = 0b00111100   # seats 4,5,6,7
        RIGHT = 0b11110000  # seats 6,7,8,9
        
        total = 0
        
        for row, mask in row_masks.items():
            if (mask & LEFT) == 0 and (mask & RIGHT) == 0:
                total += 2
            elif (mask & LEFT) == 0 or (mask & MID) == 0 or (mask & RIGHT) == 0:
                total += 1
            # else: 0 groups fit in this row
        
        rows_with_reservations = len(row_masks)
        total += (n - rows_with_reservations) * 2
        
        return total
