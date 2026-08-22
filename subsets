class Solution(object):
    def subsets(self, nums):
        result= [[]]
        for num in nums:
            temp=[]
            for sub in result:
                temp.append(sub + [num])
            result+=temp
        return result

        
