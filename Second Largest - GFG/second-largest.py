#User function Template for python3
class Solution:

	def print2largest(self,arr, n):
		# code here
		
		if n == 1 or n == 0:
		    return -1
		if n == 2:
		    return arr[1]
		
		first = -1
		second = -1
		
		for i in arr:
		    if i > first:
		        second = first
		        first = i
		    
		    if i < first and i> second:
		        second = i
		    
	    return second
		
		 
		  


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends