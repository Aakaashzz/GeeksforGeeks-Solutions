#User function Template for python3
class Solution:
    def permutation(self,s):
        lis=[]
        
        
        def permute(ch,i):
            n=len(ch)
            if (i==n-1):
                lis.append(''.join(ch))
            for j in range(i,n):
                ch[i],ch[j]=ch[j],ch[i]
                permute(ch,i+1)
                ch[i],ch[j]=ch[j],ch[i]
        
        ch=list(s) # better way to split a string than using .split()
        permute(ch,0)
        lis.sort()
        return lis


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    while(T>0):
        s=input()
        ob=Solution()
        ans=ob.permutation(s)
        for i in ans:
            print(i,end=" ")
        print()
        
        T-=1
# } Driver Code Ends