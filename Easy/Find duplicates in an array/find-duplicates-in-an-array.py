from collections import defaultdict

class Solution:
    def duplicates(self, arr, n): 
        result = []
        flag = 0
        freq = defaultdict(int)
        for num in arr:
            freq[num]+=1
        for first, second in freq.items():
            if second>1:
                flag+=1
                result.append(first)
        if flag == 0:
            return [-1]
        return sorted(result)


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends