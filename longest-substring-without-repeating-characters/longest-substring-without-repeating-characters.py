class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr=list(s)
        arr1=[]
        ans=0
        for k in range(0,len(arr)):
            i=arr[k]
            if i in arr1:
                if len(arr1) >= ans:
                    ans=len(arr1)
                   
              
                ind=arr1.index(i)
                sliceobj=slice(ind+1,len(arr1))
                arr1=arr1[sliceobj]
                
                arr1.append(i)
                    
            else:
                arr1.append(i)
       
        if len(arr1)>ans:
            ans=len(arr1)
        return ans
        