class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 32-bit signed integer range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Handle overflow: only case is INT_MIN / -1
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determine sign of result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values
        dvd = abs(dividend)
        dvs = abs(divisor)

        result = 0

        while dvd >= dvs:
            temp = dvs
            multiple = 1

            # Double the divisor (bit shift) until it exceeds dvd
            while dvd >= (temp << 1):
                temp <<= 1
                multiple <<= 1

            dvd -= temp
            result += multiple

        return -result if negative else result
