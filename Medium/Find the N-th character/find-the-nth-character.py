#User function Template for python3

class Solution:
    def nthCharacter(self, s, r, n):
        temp_str = s
        for i in range(r):
            temp_str = ''.join("01" if temp_str[i]=='0' else "10" for i in range((n//2)+1))
        return temp_str[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        snr = input().split()
        S, R, N = snr[0], int(snr[1]), int(snr[2])
        ob = Solution()
        print(ob.nthCharacter(S, R, N))
# } Driver Code Ends