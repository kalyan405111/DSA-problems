class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        # Take the first string as reference
        prefix = strs[0]

        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]  # remove last character
                if not prefix:
                    return ""

        return prefix
