#User function Template for python3

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        visited=set()
        ans=[]
        queue=[]
        queue.append(0)
        visited.add(0)
        while(len(queue)!=0):
            ans.append(queue[0])
            for i in adj[queue[0]]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
            del queue[0]
        return ans

#{ 
#  Driver Code Starts
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
		ob = Solution()
		ans = ob.bfsOfGraph(V, adj)
		for i in range(len(ans)):
		    print(ans[i], end = " ")
		print()
        

# } Driver Code Ends