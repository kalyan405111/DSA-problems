class Solution:
    def uniquePrimeFactors(self, n):
        factors = []
        d = 2
        while d * d <= n:
            if n % d == 0:
                factors.append(d)
                while n % d == 0:
                    n = n // d
            d += 1
        if n > 1:
            factors.append(n)
        return factors


sol = Solution()
print(sol.uniquePrimeFactors(100))  # [2, 5]
print(sol.uniquePrimeFactors(60))   # [2, 3, 5]
print(sol.uniquePrimeFactors(29))   # [29]
