#User function Template for python3
'''
	Function to merge two sorted lists in one
	using constant space.
	
	Function Arguments: head_a and head_b (head reference of both the sorted lists)
	Return Type: head of the obtained list after merger.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

'''
def sortedMerge(head1, head2):
    temp1=head1
    temp2=head2
    st1=[]
    st2=[]
    while temp1 is not None:
        st1.append([temp1,temp1.data])
        temp1=temp1.next
    while temp2 is not None:
        st1.append([temp2,temp2.data])
        temp2=temp2.next
    st1.sort(key=lambda x:x[1])
    st2.sort(key=lambda x:x[1])
    for i in range(len(st1)-1):
        st1[i][0].next=st1[i+1][0]
        
    for i in range(len(st2)-1):
        st2[i][0].next=st2[i+1][0]
    
    if len(st2)>0:
         st2[-1][0].next=None
         st1[-1][0]=st2[0][0]
    
    return st1[0][0]

##list of tuple is used to store and access LL.

#{ 
 # Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends