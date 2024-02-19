#User function Template for python3
import heapq
from collections import Counter

class Solution:
    def minValue(self, s, k):
        counter = Counter(s)
        counts = [-v for v in counter.values()]
        heapq.heapify(counts)
        
        while k > 0:
            max_count = heapq.heappop(counts)
            heapq.heappush(counts, max_count+1)
            k -= 1
        
        return sum(i**2 for i in counts)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends