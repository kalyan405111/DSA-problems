class Solution(object):
    def reverseBits(self, n):
        # pad to 32 bits, then reverse the string
        bb = bin(n)[2:].zfill(32)  # strip '0b', pad to 32 bits
        reversed_bb = bb[::-1]
        return int(reversed_bb, 2)  # convert back to int
