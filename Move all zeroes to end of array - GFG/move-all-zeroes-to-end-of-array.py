#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr, n):
    	# code here
    	ans = []
    	zeroCount = 0
    	for i in arr:
    	    if i == 0:
    	        zeroCount = zeroCount + 1
    	    else:
    	        ans.append(i)
        for x in range(zeroCount):
            ans.append(0)
        arr[:]=ans
    	        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends