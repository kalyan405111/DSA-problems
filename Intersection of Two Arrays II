class Solution:
    def intersect(self, nums1, nums2):
        freq = {}

        for i in nums1:
            freq[i] = freq.get(i, 0) + 1

        result = []

        for i in nums2:
            if freq.get(i, 0) > 0:
                result.append(i)
                freq[i] -= 1

        return result
