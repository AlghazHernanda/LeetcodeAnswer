# https://velog.io/@limelimejiwon/Leetcode994.-Rotting-Oranges
# https://leetcode.com/problems/rotting-oranges/

class Solution:
   def orangesRotting(self, grid: List[List[int]]) -> int:
        R,C =len(grid), len(grid[0])
        rotten=[]
        # find rotten oranges
        for i in range(R):
            for j in range(C):
                if grid[i][j]==2: 
                    rotten.append((i,j))

        minute=0
        while rotten:
            adj_q=[]
            while rotten:
                position=rotten.pop(0)
                r,c=position[0],position[1]
                # check if its neighbor are fresh
                if r+1<R and grid[r+1][c]==1: 
                    grid[r+1][c]=2
                    adj_q.append((r+1,c))
                if r-1>=0 and grid[r-1][c]==1: 
                    grid[r-1][c]=2
                    adj_q.append((r-1,c))
                if c+1<C and grid[r][c+1]==1: 
                    grid[r][c+1]=2
                    adj_q.append((r,c+1))
                if c-1>=0 and grid[r][c-1]==1: 
                    grid[r][c-1]=2
                    adj_q.append((r,c-1))
            # if all the adjacent cell got rotten, 1 minute pass
            if adj_q:
                minute+=1
                rotten.extend(adj_q)
        
        # If there is fresh orange left then return -1
        for i in range(R):
            for j in range(C):
                if grid[i][j]==1:
                    return -1

        return minute      