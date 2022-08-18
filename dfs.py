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
    
    # 235 Lowest Common Ancestor of a Binary Search Tree
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # the LCA must be within the range of p, q
        # otherwise p and q would be on the same sub-tree of that node
        m1 = min(p.val, q.val)
        m2 = max(p.val, q.val)
        
        while root != None: 
            if root.val < m1: 
                root = root.right
            elif root.val > m2: 
                root = root.left
            else: 
                return root
        return None
    
    # 98 Validate Binary Search Tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, low = -math.inf, high = math.inf): 
            if root == None: 
                return True
            if (root.val <= low) or (root.val >= high):
                return False
            return (valid(root.left, low, root.val)) and (valid(root.right, root.val, high))
        
        return valid(root)

    # 78. Subsets
    def subsets(self, nums: List[int]) -> List[List[int]]:
    
        def helper(nums, s, idx, result): 
            if idx == len(nums): 
                result.append(s)
                return
            # not add the char at idx to s
            helper(nums, s, idx+1, result)
            # add the char at idx to s
            s = s + [nums[idx]]
            helper(nums, s, idx+1, result)
            # remove the char at idx before going back to previous level
            s = s[:len(s)-1]
            
        result = []
        if len(nums) <= 0: 
            return result
        s = [] # initialize a subset
        helper(nums, s, 0, result)
        return result
    
    # 22. Generate Valid Parentheses
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(cur, left, right, result): 
            if left == 0 and right == 0: 
                result.append(cur)
                return
            if left > 0: 
                cur = cur + '('
                helper(cur, left - 1, right, result)
                cur = cur[:-1]
            if right > left: 
                cur = cur + ')'
                helper(cur, left, right - 1, result)
                cur = cur[:-1]
                
        result = []
        cur = ''
        helper(cur, n, n, result)
        return result
    
    # 518. Coin Change 2
    def change(self, amount: int, coins: List[int]) -> int:
        def helper(amount, coins, idx, cur, result): 
            if idx == len(coins)-1: 
                if amount % coins[idx] == 0: 
                    cur = cur + [amount / coins[idx]]
                    result.append(cur)
                    cur = cur[:-1]
                return
            # max number of current coin
            m = amount // coins[idx]
            for i in range(m+1): 
                cur = cur + [i]
                helper(amount - i * coins[idx], coins, idx+1, cur, result)
                cur = cur[:-1]
                
        result = []
        cur = []
        helper(amount, coins, 0, cur, result)
        # return result
        return len(result)
    
    # 46. Permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        def swap(arr, i, j):
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            return arr
        
        def helper(arr, idx, result): 
            if idx == len(arr): 
                tmp = arr.copy()
                result.append(tmp)
                return
            for i in range(idx, len(arr)): 
                arr = swap(arr, idx, i)
                helper(arr, idx + 1, result)
                arr = swap(arr, idx, i)

        result = []
        helper(nums, 0, result)
        return result
                
