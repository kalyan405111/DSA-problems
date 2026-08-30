class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        max_xor = 0
        mask = 0

        for bit in range(31, -1, -1):  # 32-bit integers, start from MSB
            mask |= (1 << bit)  # extend mask to include this bit
            prefixes = {num & mask for num in nums}  # prefixes up to this bit

            candidate = max_xor | (1 << bit)  # try assuming this bit can be 1

            # Check if any two prefixes XOR to give us this candidate
            found = False
            for prefix in prefixes:
                if (candidate ^ prefix) in prefixes:
                    found = True
                    break

            if found:
                max_xor = candidate  # confirmed, keep this bit set

        return max_xor
