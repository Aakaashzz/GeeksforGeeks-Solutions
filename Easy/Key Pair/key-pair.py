class Solution:
	def hasArrayTwoCandidates(self,arr, n, x):
		new_set=set()
		for i in range(n):
		    target=x-arr[i]
		    if target in new_set:
		        return True
	        new_set.add(arr[i])
	    return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.hasArrayTwoCandidates(arr, n, x)
        if ans:
            print("Yes")
        else:
            print("No")
        tc -= 1

# } Driver Code Ends