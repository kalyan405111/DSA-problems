from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        groups = defaultdict(list)
        
        for s in strs:
            # Count occurrences of each letter (26 lowercase letters)
            count = [0] * 26
            for char in s:
                count[ord(char) - ord('a')] += 1
            
            # Use the count tuple as a key — anagrams share the same key
            key = tuple(count)
            groups[key].append(s)
        
        return list(groups.values())
