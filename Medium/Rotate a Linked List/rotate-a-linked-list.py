# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


class Solution:
    
    #Function to rotate a linked list.
    def rotate(self, head, k):
        #take example number 1->2->3->4->->5->6
        curr = head#1
        second = head.next#2
        count = 1
        while count<k:#1<k k value is 3 just assume
            curr = curr.next#1->2->3
            second = second.next#4->5->6
            count+=1#increment 1
        if curr.next is None:#1->2->3

            return head #go back
        curr.next = None
        
        dummy = Node(0)#0
        tail = dummy#0
        first = head#1->2->3
        tail.next = second#->0->4->5->6
        temp = second#->4->5->6
        while temp and temp.next:
            temp = temp.next
        temp.next = first#0->4->5->6->1->2->3
        return dummy.next#4->5->6->1->2->3


#{ 
 # Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = Solution().rotate(lis.head,k)
        printList(head)
# } Driver Code Ends