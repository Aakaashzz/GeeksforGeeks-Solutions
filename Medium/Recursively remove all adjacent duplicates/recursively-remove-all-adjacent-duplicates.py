#User function Template for python3

class Solution:
    def rremove (self, S):
	    n = len(S)
	    
	    t = ''
	    i = 0
	    while i < n:
	        loop = False
	        while i+1 < n and S[i] == S[i+1]:
	            loop = True
	            i += 1
	            
	        if loop:
	            i += 1
	            continue
	        
	        if i < n:
	            t += S[i]
	        i += 1
	        
	    if t == S:
	        return t
	    
	    x = self.rremove(t)
	    
	    return x




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        S = input()
        ob = Solution()
        print(ob.rremove(S))


# } Driver Code Ends