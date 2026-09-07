class Solution(object):
    def twoSum(self, numbers, target):
        l=0
        r=len(numbers) -1
        while l<r:
            current= numbers[l]  + numbers[r]
            if current == target:
                return [l+1,r+1]
            elif current <target:
                l+=1
            else:
                r-=1
   
    

        