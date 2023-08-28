
class Solution:
    def countDistinct(self, A, N, K):
        # Code here
        res=[]
        ans = {}
        dist_count=0
        
        for i in range(0,k):
            if A[i] in ans:
                ans[A[i]] +=1
            else:
                ans[A[i]] =1
                dist_count +=1
        res.append(dist_count)
        
        j=0
        
        
        for i in range(k,N):
            if A[j] in ans:
                
                if ans[A[j]] == 1:
                    print
                    dist_count -=1
                    ans[A[j]] = 0
                else:
                    ans[A[j]] -= 1
                    
            if A[i] in ans and ans[A[i]] != 0:
                ans[A[i]] +=1
            else:
                ans[A[i]] =1
                dist_count +=1
            j+=1
            
            res.append(dist_count)
            
        return res
        
        


#{ 
 # Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n,k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        res = Solution().countDistinct(arr, n, k)
        for i in res:
            print (i, end = " ")
        print ()
# } Driver Code Ends