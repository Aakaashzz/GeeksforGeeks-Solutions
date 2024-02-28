class Solution:
    def DivisibleByEight(self,s):
        num=int(s[-3:])
        return 1 if num%8==0 else -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        S=input()
        ob=Solution()
        print(ob.DivisibleByEight(S))
# } Driver Code Ends