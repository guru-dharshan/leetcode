from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph=defaultdict(list)
        for i in trust:
            s=i[0]
            e=i[1]
            graph[s].append(e)
        k=-1
        for i in range(1,n+1):
            #condition 1
            if len(graph[i])==0:
                k=i
        for i in range(1,n+1):
            if i!=k:
                if k not in graph[i]:
                    return -1
        return k
            
            
            
            
        
        