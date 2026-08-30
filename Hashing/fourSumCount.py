class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        freq ={}
        for i in nums1:
            for j in nums2:
                total= i +j
                freq[total] = freq.get(total,0)+1
        
        count =0
        for i in nums3:
            for j in nums4:
                total =i +j
                count+= freq.get(-total,0)
        return count
