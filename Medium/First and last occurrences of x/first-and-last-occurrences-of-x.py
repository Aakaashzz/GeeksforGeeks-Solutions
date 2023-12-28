#User function Template for python3


class Solution:
    def find(self, arr, n, x):
        
        # code here
        b=[]
        first=-1
        last=-1
        count=0
        for i in range(0,n):
            if(arr[i]==x):
                count=count+1
                if(count==1):
                    first=i
                last=i
        b.append(first)
        b.append(last)
        return b

#{ 
 # Driver Code Starts
t=int(input())
for _ in range(0,t):
    l=list(map(int,input().split()))
    n=l[0]
    x=l[1]
    arr=list(map(int,input().split()))
    ob = Solution()
    ans=ob.find(arr,n,x)
    print(*ans)
# } Driver Code Ends