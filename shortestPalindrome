class Solution(object):
    def shortestPalindrome(self, s):
        if not s:
            return s
        
        rev_s = s[::-1]
        combined = s + '#' + rev_s
        n = len(combined)
        
        # build KMP failure function
        fail = [0] * n
        for i in range(1, n):
            j = fail[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = fail[j - 1]
            if combined[i] == combined[j]:
                j += 1
            fail[i] = j
        
        palindrome_len = fail[-1]
        to_add = rev_s[:len(s) - palindrome_len]
        
        return to_add + s
