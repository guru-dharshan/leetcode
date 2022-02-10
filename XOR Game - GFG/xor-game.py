#User function Template for python3

class Solution:
    def xorCal(self, k):
        # code here
        n=k//2
        if k==1:
            return 2
        if(n^n+1==k):
            return n
        return -1
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        k = int(input())
        
        ob = Solution()
        print(ob.xorCal(k))
# } Driver Code Ends