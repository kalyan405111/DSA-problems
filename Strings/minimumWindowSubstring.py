class Solution(object):
    def minWindow(self, s, t):
    
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        have = {}
        formed = 0
        required = len(need)

        left = 0
        min_len = float('inf')
        ans = ""

        for right in range(len(s)):
            ch = s[right]
            have[ch] = have.get(ch, 0) + 1

            if ch in need and have[ch] == need[ch]:
                formed += 1

            while formed == required:
                window_len = right - left + 1
                if window_len < min_len:
                    min_len = window_len
                    ans = s[left:right+1]

                left_char = s[left]
                have[left_char] -= 1
                if left_char in need and have[left_char] < need[left_char]:
                    formed -= 1
                left += 1

        return ans
