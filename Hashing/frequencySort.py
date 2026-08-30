class Solution(object):
    def frequencySort(self, s):
        result = ""
        hash_map = {}
        
        for ch in s:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        
        sort = sorted(hash_map.items(), key=lambda x: x[1], reverse=True)
        
        for chars, freq in sort:
            result += chars * freq
        
        return result
