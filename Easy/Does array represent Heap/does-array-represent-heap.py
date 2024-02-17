class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here   
        for i in range(1, n):
            parent = (i + 1) // 2
            if arr[parent - 1] < arr[i]:
                return False
                
        return True


#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends