#User function Template for python3
class Solution:

	def segregateEvenOdd(self,arr, n):
		# code here
		##approch 1
		evenarr=[]
		oddarr=[]
		arr.sort()
		for i in arr:
		    if i% 2 == 0:
		        evenarr.append(i)
		    else:
		        oddarr.append(i)
	    arr[:]=evenarr+oddarr


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.segregateEvenOdd(arr, n)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends