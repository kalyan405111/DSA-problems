class Solution:
    def fun(self, x):
        sign = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        s = str(x)
        n = int(s[::-1])
        if n > ((2**31) - 1):
            return 0
        return n * sign


sol = Solution()
x = -120
print(sol.fun(x))
