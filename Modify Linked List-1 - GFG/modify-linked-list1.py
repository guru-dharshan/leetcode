#User function Template for python3

"""
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    #Function to reverse a linked list.
    def modifyTheList(self, head):
        # Code here
        p=head
        f=head
        c=0
        while(f!=None and f.next!=None):
            p=p.next
            f=f.next.next
            c=c+1
        middle=p
        
        if f==None:
            count=(c*2)+1
        else:
            count=c*2
        
        li=[]
        l=[]
        if(count%2==0):
            p=p.next
            middle=p
        
        while(p!=None):
            li.append(p.data)
            p=p.next
        
        temp=head
        
        for i in range(0,(count//2)):
            t=li.pop()
            l.append(temp.data)
            temp.data=t-temp.data
            temp=temp.next
        for i in range(0,(count//2)):
            t=l.pop()
            
            middle.data=t
            middle=middle.next
        return head
            
            
        
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

# Node Class    
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp=tmp.next
    print()

if __name__=='__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        
        lis = Linked_List()
        for i in arr:
            lis.insert(i)
        
        newHead = Solution().modifyTheList(lis.head)
        printList(newHead)

# } Driver Code Ends