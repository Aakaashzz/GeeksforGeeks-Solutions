from itertools import combinations
class Solution:
    def AllPossibleStrings(self, s):
        ans=[]
        for i in range(1,len(s)+1):
            comb=combinations(s,i)
            for j in comb:
                ans.append("".join(j))
        return sorted(ans)


#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends