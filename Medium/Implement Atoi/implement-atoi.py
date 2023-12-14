#User function template for Python

class Solution:
    def atoi(self,string):
        a=""
        if string[0]=="-":
            a+="-"
            aa="1234567890"
            for i in string[1:]:
                if (i) in aa:
                    a+=i
                else:
                    return -1
            return int(a)
        else:
            aa="1234567890"
            for i in string:
                if (i) in aa:
                    a+=i
                else:
                    return -1
            return int(a)
            
#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends