class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        arr=[]
        for i in range(0,len(nums)):
            no=target-nums[i]
            if(no in nums):
                j=nums.index(no)
                if i!=j: 
                    arr.append(i)
                    arr.append(j)
               
                    return arr
            
            
                
                    