class Solution(object):
    def countPrimes(self, n):
        if n < 3:
            return 0
        
        # Assume every number from 0 to n-1 is prime initially
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(n ** 0.5) + 1):
            if is_prime[i]:
                # Cross off all multiples of i, starting from i*i
                for multiple in range(i*i, n, i):
                    is_prime[multiple] = False
        
        return sum(is_prime)


sol = Solution()
print(sol.countPrimes(10))  # 4
print(sol.countPrimes(0))   # 0
print(sol.countPrimes(1))   # 0
