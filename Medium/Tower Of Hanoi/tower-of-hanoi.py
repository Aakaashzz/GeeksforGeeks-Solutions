# User function Template for python3

import sys
sys.setrecursionlimit(10**6)
class Solution:
    def toh(self, N, fromm, to, aux):
        count = 0  # Initialize count as a local variable
        
        if N == 0:
            return count

        if N == 1:
            print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))

            count += 1
            return count

        count += self.toh(N - 1, fromm, aux, to)
        print("move disk " + str(N) + " from rod " + str(fromm) + " to rod " + str(to))

        count += 1
        count += self.toh(N - 1, aux, to, fromm)
        
        return count

#{ 
 # Driver Code Starts
# Initial Template for Python 3


import math


def main():

    T = int(input())

    while(T > 0):
        N = int(input())
        ob = Solution()
        print(ob.toh(N, 1, 3, 2))
        T -= 1
if __name__ == "__main__":
    main()


# } Driver Code Ends