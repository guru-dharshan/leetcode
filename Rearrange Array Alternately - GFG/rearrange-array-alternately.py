#User function Template for python3
class Solution:
    ##Complete this function
    #Function to rearrange  the array elements alternately.
    def rearrange(self,arr, n): 
        ##Your code here
        ans=[]
        endIndex = len(arr) - 1
        for staringIndex in range(0,len(arr) // 2):
            ans.append(arr[endIndex])
            ans.append(arr[staringIndex])
            endIndex = endIndex - 1
        if(len(arr) % 2 !=0):
             ans.append(arr[endIndex])
            
        arr[:]=ans
            
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math




def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends