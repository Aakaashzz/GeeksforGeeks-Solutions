#User function Template for python3

"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""
class Solution:
    #Function to reverse a linked list.
    def arrangeCV(self, head):
        con=Node(1)
        vow=Node(1)
        vowN,conN=vow,con
        curr=head
        
        while curr:
            if curr.data == 'a' or curr.data == 'e' or curr.data == 'i' or curr.data == 'o' or curr.data == 'u':
                vowN.next=curr
                vowN=curr
            else:
                conN.next=curr
                conN=curr
            curr=curr.next
        conN.next=None
        vowN.next=con.next
        return vow.next
        


#{ 
 # Driver Code Starts
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
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [str(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newHead = Solution().arrangeCV(lis.head)
        printList(newHead)

# } Driver Code Ends