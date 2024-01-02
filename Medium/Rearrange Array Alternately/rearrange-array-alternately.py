#User function Template for python3
class Solution:
    def rearrange(self,arr, n):
        if n==1:
            return arr[0]
        arr.sort()
        i=0
        li=[]
        j=n-1
        while i<n and j>=i:
            li.append(arr[j])
            li.append(arr[i])
            i+=1
            j-=1
        arr[:]=li[0:n] 



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
            ob.rearrange(arr,n)
            
            for i in arr:
                print(i,end=" ")
            
            print()
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends