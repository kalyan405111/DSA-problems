class Solution:
    def getMinMax(self, arr):
        n = sorted(arr)
        return [n[0],n[-1]]
        
