class Solution(object):
    def firstUniqChar(self, s):
        hash = {}

        # Count frequency
        for i in s:
            hash[i] = hash.get(i, 0) + 1

        # Find first unique character
        for i in range(len(s)):
            if hash[s[i]] == 1:
                return i

        return -1
