#User function Template for python3
class Solution:
    
    def findUnion(self, arr1, arr2, n, m):
        # Convert arrays to sets to remove duplicates
        s1 = set(arr1)
        s2 = set(arr2)
        
        # Union of two sets
        union_set = s1.union(s2)
        
        # Convert set back to list and sort
        result = sorted(list(union_set))
        
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Contributed by : Nagendra Jha
# Modified by : Sagar Gupta


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,m = map(int,input().strip().split())
        a = list(map(int,input().strip().split()))
        b = list(map(int,input().strip().split()))
        ob=Solution()
        li = ob.findUnion(a,b,n,m)
        for val in li:
            print(val, end = ' ')
        print()
# } Driver Code Ends