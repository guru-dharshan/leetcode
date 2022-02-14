#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        
        arr.sort()
        
        number=1
        prev=0
        missing=0
        repeating=0
        for i in arr:
            
            if prev==i:
                repeating=i
                number=number-1
                
              
            elif number!=i:
                missing=number
                number=number+1
              
            number=number+1
            prev=i
            
        if prev!=n:
            missing=n
        arr=[]
        arr.append(repeating)
        arr.append(missing)
        return arr
                
                
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends