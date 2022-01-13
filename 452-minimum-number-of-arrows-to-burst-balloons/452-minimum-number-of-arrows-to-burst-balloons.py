def m1(point):
    
    c=0
    
    for i in range(0,len(point)):
        p=point[i][0]
        if point[i]!=[0,0]:
            c=c+1
            point[i]=[0,0]
            for k in range(0,len(point)):
                if p>= point[k][0] and p<=point[k][1]:
                    point[k]=[0,0]

    return c

def m2(point):
    c=0
   
    for i in range(0,len(point)):
        p=point[i][1]
        if point[i]!=[0,0]:
            c=c+1
            point[i]=[0,0]
            for k in range(0,len(point)):
                if p>= point[k][0] and p<=point[k][1]:
                    point[k]=[0,0]

    return c
    
    
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
       
        points.sort(key=lambda p: p[1])
        arrow=points[0][1]
        c=1
        for i in points:
            if arrow >=i[0] and arrow <=i[1]:
                c=c
                
            else:
                arrow=i[1]
                c=c+1
        return c
                
      
        
            
                
        