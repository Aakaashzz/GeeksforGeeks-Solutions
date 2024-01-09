#User function Template for python3

class Solution:
    def activitySelection(self,n,start,end):
        li=[]
        for i in range(n):
            k=[start[i], end[i]]
            li.append(k)
        li.sort(key=lambda x:x[1])
        z=0
        c=1
        for j in range(1,n):
            if li[j][0]>li[z][1]:
                c+=1
                z=j
        return c


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.activitySelection(n,start,end))
# } Driver Code Ends