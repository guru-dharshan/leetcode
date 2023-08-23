#User function Template for python3

#Function to find a continuous sub-array which adds up to a given number.
class Solution:
    def subArraySum(self,arr, n, s): 
        
        ans=[]
        start = 0
        c = 0
        for i in range(0,n):
           
            c= c+ arr[i]
            while c > s and start <= i:
                c = c - arr[start]
                start = start + 1
            if c==s:
                ans.append(start+1)
                ans.append(i+1)
                break
            
            
            
            
        
        if len(ans) == 0 or s==0:
            return [-1]
        return ans
           
           





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            NS=input().strip().split()
            N=int(NS[0])
            S=int(NS[1])
            
            A=list(map(int,input().split()))
            ob=Solution()
            ans=ob.subArraySum(A, N, S)
            
            for i in ans:
                print(i, end=" ")
                
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends