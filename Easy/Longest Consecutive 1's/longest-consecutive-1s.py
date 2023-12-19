#User function Template for python3


class Solution:
    ##Complete this function
    # Function to calculate the longest consecutive ones
    def maxConsecutiveOnes(self, n):
        ##Your code here
        ans=0;curr=0
        while n:
            v=n&1
            if v==0:
                ans=max(ans,curr)
                curr=0
            else:
                curr+=1
            n>>=1
        return max(ans,curr)
        
        
        
        





#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math





def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        obj = Solution()
        print(obj.maxConsecutiveOnes(n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends