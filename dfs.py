# dfs
class Solution:
    # 200 number of islands in matrix
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
    
    # 236 lowest common ancester
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def lca(root, p, q): 
            if root in [None, p, q]: 
                return root
            
            l = lca(root.left, p, q)
            r = lca(root.right, p, q)
            
            if (l != None) and (r != None): 
                return root
            if l != None: 
                return l
            else: 
                return r
            
        return lca(root, p, q)
    
    # 98 Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low = -math.inf, high = math.inf): 
            if root == None: 
                return True
            if (root.val <= low) or (root.val >= high):
                return False
            return (valid(root.left, low, root.val)) and (valid(root.right, root.val, high))
        
        return valid(root)
                
