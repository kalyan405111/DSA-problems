class Solution(object):
    def lengthOfLongestSubstring(self, s):
        unq= set()
        start =0
        max_length =0
        for end in range(len(s)):
            while s[end] in unq:
                unq.remove(s[start])
                start+=1

            
            unq.add(s[end])
            length = end - start + 1
            max_length = max(max_length , length)  
        return max_length


