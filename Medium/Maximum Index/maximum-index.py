#User function Template for python3

class Solution:
    def maxIndexDiff(self, arr, n):
        """
        Find the maximum index difference in the given array.

        Parameters:
        - arr (List[int]): The input array.
        - n (int): The length of the array.

        Returns:
        - int: The maximum index difference.
        """
        # Early return for empty array
        if not arr:
            return -1

        # Initialize variables
        left_min = [0] * n
        right_max = [0] * n

        # Calculate the minimum value from the left
        left_min[0] = arr[0]
        for i in range(1, n):
            left_min[i] = min(left_min[i - 1], arr[i])

        # Calculate the maximum value from the right
        right_max[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], arr[i])

        # Initialize variables for iterating through the arrays
        i = 0
        j = 0
        max_index_diff = -1

        # Iterate through the arrays and find the maximum index difference
        while i < n and j < n:
            if left_min[i] <= right_max[j]:
                max_index_diff = max(max_index_diff, j - i)
                j += 1
            else:
                i += 1

        return max_index_diff

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            ob=Solution()
            print(ob.maxIndexDiff(arr,n))
            
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends