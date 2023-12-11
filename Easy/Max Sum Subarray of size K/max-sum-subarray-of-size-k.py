class Solution:
    def maximumSumSubarray (self,k,arr,n):
        res=0
        sum=0
        for i in range(n):
            if i<k:
                sum+=arr[i]
            else:
                res=max(res,sum)
                sum+=arr[i]
                sum-=arr[i-k]
        res=max(res,sum)
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends