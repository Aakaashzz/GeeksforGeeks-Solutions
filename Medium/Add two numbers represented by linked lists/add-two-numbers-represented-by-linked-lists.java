//{ Driver Code Starts
// driver

import java.util.*;

class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

class GfG{
    
    static void printList(Node n){
        while(n!=null){
            System.out.print(n.data+" ");
            n = n.next;
        }
        System.out.println();
    }
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        
        while (T-- > 0) {
            
            int n = sc.nextInt();
            int val = sc.nextInt();
            
            Node first = new Node(val);
            Node tail = first;
            for(int i=0; i<n-1; i++)
            {
                val = sc.nextInt();
                tail.next = new Node(val);
                tail = tail.next;
            }
            
            int m = sc.nextInt();
            val = sc.nextInt();
            
            Node second = new Node(val);
            tail = second;
            for(int i=0; i<m-1; i++)
            {
                val = sc.nextInt();
                tail.next = new Node(val);
                tail = tail.next;
            }
            
            Solution g = new Solution();
            Node res = g.addTwoLists(first, second);
            printList(res);
        }
    }
}

// } Driver Code Ends


/* node for linked list

class Node {
    int data;
    Node next;

    Node(int d) {
        data = d;
        next = null;
    }
}

*/

class Solution{
    static Node reverse(Node head){
        if(head==null || head.next==null) return head;
        Node temp=head.next;
        Node rev=reverse(head.next);
        
        temp.next=head;
        head.next=null;
        return rev;
        
    }
    static Node addTwoLists(Node first, Node second){
        Node head=null;
        Node temp=head;
        Node head1=reverse(first);
        Node head2=reverse(second);
        Node temp1=head1;
        Node temp2=head2;
        int carry=0;
        while(temp1!=null || temp2!=null ||carry!=0){
            int sum = (temp1 != null ? temp1.data : 0) + (temp2 != null ? temp2.data : 0) + carry;
            int num=sum%10;
            carry=sum/10;
            Node newNode=new Node(num);
            if(head==null){
                head=newNode;
                temp=head;
            }
            else{
                head.next=newNode;
                head=head.next;
            }
            if (temp1 != null) temp1 = temp1.next;
            if (temp2 != null) temp2 = temp2.next;
        }
       
        return reverse(temp);
    }
}