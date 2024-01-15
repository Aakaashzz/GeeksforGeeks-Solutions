class Solution:
    def bToDLL(self,root):
        head, tail = self.construct_dll(root)
        return head
        
        
    def construct_dll(self,root):
        # do Code here
        head = None
        tail = None
        if not root:
            return head, tail
        
        l_head, l_tail = self.construct_dll(root.left)
        root_node = root
        r_head, r_tail= right_node = self.construct_dll(root.right)
        
        if (not l_head) and (not r_head):
            head = root_node
            tail = root_node
            
        if l_head :
            l_tail.right = root_node
            root_node.left = l_tail
            head = l_head
            tail = root_node
        else:
            head = root_node
            tail = root_node

        if r_head:
            tail.right = r_head
            r_head.left = tail
            tail = r_tail # or tail.right
        
        return head, tail


#{ 
 # Driver Code Starts
#Initial template for Python

from collections import deque
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root


import sys            
def printDLL(head): #Print util function to print Linked List
    prev = None
    sys.stdout.flush()
    while(head != None):
        print(head.data, end=" ")
        prev=head
        head=head.right
    print('')
    while(prev != None):
        print(prev.data, end=" ")
        prev=prev.left
    print('')
    
if __name__=='__main__':
    t=int(input())
    for _ in range(0,t):
        s=input()
        root=buildTree(s)
        ob = Solution()
        head = ob.bToDLL(root)
        printDLL(head)
# } Driver Code Ends