class Solution:
   
    def longestPalindrome(self, s: str) -> str:
        arr=s
        check=""
        ans="" 
        pali=""
        cout=0
        for i in range(0,len(arr)):
            check=""
            check=arr[i:]   
            if len(check) >len(pali) and check.count(check[0])>1:
                ans=""
                for j in range(0,len(check)):                 
                    ans+=check[j]
                    
                    ispalindrome=checkpalindrome(ans)
                    if ispalindrome and len(pali)<len(ans):
                        pali=ans[:]         
        if len(pali) == 0:
            return arr[0]
        else:
            s=""
            return pali                     
def checkpalindrome(arr):
    return arr==arr[: : -1]
        
    