#User function Template for python3

class Solution:
    def longestSubstring(self, s , N):
        max_length = 0
        ans= "-1"
        i,j = 0,0
        
        while i<N and j<N:
            
            ss = s[i:j+1]
            
            if s.find(ss,j+1)!=-1:
                
                length = len (ss)
                
                if length > max_length:
                    
                    ans = ss
                    max_length = length
                    
            else:
                i+=1
            j+=1
            
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        S=input()
        
        ob = Solution()
        print(ob.longestSubstring(S , N))
# } Driver Code Ends