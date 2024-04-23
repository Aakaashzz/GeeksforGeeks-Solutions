#User function Template for python3
class Solution:
    def MedianOfArrays(self, a, b):
            #code here
            c=sorted(a+b)
            m=len(c)//2
            if len(c)%2==0:
                if int((c[m]+c[m-1])/2)==(c[m]+c[m-1])/2:
                    return int((c[m]+c[m-1])/2)
                else:
                    return (c[m]+c[m-1])/2
            else:
                return c[m]

fgkkpoijh67890oiuhg
#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tcs=int(input())

    for _ in range(tcs):
        m = input()
        arr1=[int(x) for x in input().split()]
        n = input()
        arr2=[int(x) for x in input().split()]
        
        
        ob = Solution()
        print(ob.MedianOfArrays(arr1,arr2))

# } Driver Code Ends