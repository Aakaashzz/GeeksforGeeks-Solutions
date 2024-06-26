#User function Template for python3

def circularSubarraySum(arr,n):
    ##Your code here
    # approach - 
    # 1. apply kadanes on the initial array, say k
    # if k < 0 return k
    # 2. else find arr sum and negate all the elements 
    # 3. find kadane of negate elements
    # circular = 2 + 3
    # return max of t and circular 
    
    def kadane(arr, n):
        curr = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            
            if curr < 0:
                curr = arr[i]
            else:
                curr += arr[i]
            
            result = max(result, curr)
        
        return result
        
    def mini(arr, n):
        curr = arr[0]
        result = arr[0]
        
        for i in range(1, n):
            if curr > 0:
                curr = arr[i]
            else:
                curr += arr[i]
            
            result = min(curr, result)
        
        return result
        
    def circular(arr, n):
        
        initial = kadane(arr, n)
        
        if initial < 0:
            return initial
            
        arr_sum = 0
        for i in range(n):
            arr_sum += arr[i]
        
        after = mini(arr, n)
        
        max_circular = arr_sum - after
        
        return max(initial, max_circular)
        
    return circular(arr, n)


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math
import sys

    
    

if __name__ == "__main__":
    T=int(input())
    while(T>0):
            
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
            
        print(circularSubarraySum(arr,n))
        
        T-=1
    
# } Driver Code Ends