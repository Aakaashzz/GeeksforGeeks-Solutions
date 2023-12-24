class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        s1=S.split(".")
        s1.reverse()
        
                
        return ".".join(s1)

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends