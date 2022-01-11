# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

arr=[]
def check(root,binary):
    if root!=None:
        binary=binary+str(root.val)
        check(root.left,binary)
        check(root.right,binary)
        if root.left ==None and root.right==None:
            arr.append(binary)
        
        binary=binary[:len(binary)-1]


    
class Solution:
    
   
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
       
        binary=""
        sum=0
        check(root,binary)
        for i in arr:
            print(i)
            a=int(i,2)
            sum=sum+a
        arr.clear()
            
        
        
        return sum
        