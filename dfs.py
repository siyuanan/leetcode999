# dfs
class Solution:
    # 200
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j): 
            m = len(grid)
            n = len(grid[0])
            if (i < 0) or (i >= m) or (j < 0) or (j >= n) or (grid[i][j] == '0'): 
                return
            grid[i][j] = '0'
            dfs(grid, i - 1, j)
            dfs(grid, i + 1, j)
            dfs(grid, i, j - 1)
            dfs(grid, i, j + 1)
            
        if (len(grid) <= 0): 
            return 0
        if (len(grid[0]) <= 0): 
            return 0
        
        ans = 0
        for ii in range(len(grid)): 
            for jj in range(len(grid[0])): 
                if grid[ii][jj] == '1': 
                    ans += 1
                    dfs(grid, ii, jj)
                    
        return ans
                
