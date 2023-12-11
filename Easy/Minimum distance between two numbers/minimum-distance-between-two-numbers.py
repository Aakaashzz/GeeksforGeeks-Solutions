
class Solution:
    def minDist(self, arr, n, x, y):
        s1 = -1
        s2 = -1
        l=[]
        
        if x not in arr or y not in arr:
            return -1
        else:
            for i in range(0, len(arr)):
                if x==arr[i]:
                    s1= i
                        
                if y == arr[i]:
                    s2 = i
                        
                   
                if (s1 != -1 and s2 != -1):
                    l.append(abs(s1-s2))
            l.sort()
            return l[0]        
        
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        x,y = list(map(int, input().strip().split()))
        print(Solution().minDist(arr, n, x, y))



# } Driver Code Ends