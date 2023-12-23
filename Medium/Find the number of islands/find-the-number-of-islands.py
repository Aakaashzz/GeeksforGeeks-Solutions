#User function Template for python3

from collections import deque
import sys
sys.setrecursionlimit(10**8)
class Solution:
    def numIslands(self,grid):
        #code here
        if not grid:
            return 0
        
        rows,cols=len(grid),len(grid[0])
        visit=set()
        island=0
        
        def bfs(r,c):
            q=deque()
            visit.add((r,c))
            q.append((r,c))
            while q:
                row,col=q.popleft()
                direction=[[1,0],[-1,0],[0,1],[0,-1],[1,1],[-1,1],[1,-1],[-1,-1]]
                for dr,dc in direction:
                    r,c=row+dr,col+dc
                    if (r in range(rows) and c in range(cols) and grid[r][c]==1 and (r,c) not in 
                    visit):
                        q.append((r,c))
                        visit.add((r,c))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==1 and (r,c) not in visit:
                    bfs(r,c)
                    island+=1
        return island


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n,m=map(int,input().strip().split())
        grid=[]
        for i in range(n):
            grid.append([int(i) for i in input().strip().split()])
        obj=Solution()
        print(obj.numIslands(grid))
# } Driver Code Ends