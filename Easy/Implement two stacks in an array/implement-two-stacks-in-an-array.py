#User function Template for python3

class TwoStacks:
    def __init__(self, n=100):
       self.arr = [0]*n
       self.len1 = n//2
       self.len2 = n//2
       self.i = 0        # Starting index for first stack
       self.j = n//2    # Starting index for second stack
      
    # Function to push an integer into stack 1
    def push1(self, x):
        self.arr[self.i] = x
        self.i+=1

    # Function to push an integer into stack 2
    def push2(self, x):
        self.arr[self.j] = x
        self.j+=1


    # Function to remove an element from top of stack 1
    def pop1(self):
        if self.i==0:
            return -1
        ele = self.arr[self.i-1]
        self.i-=1
        return ele
            
    # Function to remove an element from top of stack 2
    def pop2(self):
        if self.j==self.len2:
            return -1
    
        ele = self.arr[self.j-1]
        
        self.j -= 1
        return ele



#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

# } Driver Code Ends