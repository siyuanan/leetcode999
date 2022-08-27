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
    
    # 1650. Lowest Common Ancestor of a Binary Tree III with parent pointer
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # get node depth
        def depth(node): 
            d = 0
            while node != None: 
                node = node.parent
                d += 1
            return d
        
        # move the lower node the same level with high node
        def merge(low, high, diff): 
            while diff > 0: 
                low = low.parent
                diff -= 1
            # now the two nodes are the same level
            while low != high: 
                low = low.parent
                high = high.parent
            return low
        
        d1 = depth(p)
        d2 = depth(q)
        if d1 > d2: 
            return merge(p, q, d1-d2)
        else: 
            return merge(q, p, d2-d1)
    
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
    
    # 314. Binary Tree Vertical Order Traversal
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: 
            return []
        
        table = dict()
        min_col = 0
        max_col = 0
        min_row = 0
        max_row = 0
        
        # dfs
        def dfs(node, row, col): 
            nonlocal min_col, max_col, min_row, max_row
            if node != None: 
                min_col = min(col, min_col)
                max_col = max(col, max_col)
                min_row = min(row, min_row)
                max_row = max(row, max_row)
                if (row, col) not in table.keys(): 
                    table[(row, col)] = []
                table[(row, col)].append(node.val)
                
                dfs(node.left, row + 1, col - 1)
                dfs(node.right, row + 1, col + 1)
        
        dfs(root, 0, 0)
        
        result = []
        for i in range(min_col, max_col+1): 
            res = []
            for j in range(min_row, max_row+1): 
                if (j, i) in table.keys(): 
                    for n in table[(j, i)]: 
                        res.append(n)

            if len(res) > 0: 
                result.append(res)
        return result
    
    # 543. Diameter of Binary Tree
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        d = 0
        def dfs(node): 
            nonlocal d
            if node == None: 
                return 0
            left = dfs(node.left)
            right = dfs(node.right)
            d = max(d, left + right)
            return max(left, right) + 1
        dfs(root)
        return d
    
    # 339. Nested List Weight Sum
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        def dfs(lst, d): 
            s = 0
            for l in lst: 
                if l.isInteger(): 
                    s += l.getInteger() * d
                else: 
                    s += dfs(l.getList(), d+1)
            return s
        
        return dfs(nestedList, 1)
    
    
    # interview add operators
    def addOperators(self, num: str, target: int) -> List[str]:
        from collections import deque
        def calculate(s): 
            res = deque() # as a stack
            operation = '+'
            curNumber = 0
            i = 0
            
            while i < len(s): 
                while i < len(s) and s[i] >= '0' and s[i] <= '9': 
                    curNumber = 10 * curNumber + int(s[i])
                    i += 1
                
                if i < len(s):
                    if operation == '+': 
                        res.append(curNumber)
                    elif operation == '-': 
                        res.append(-curNumber)
                    elif operation == '*': 
                        res.append(curNumber * res.pop())
                    else: 
                        res.append(int(res.pop() / curNumber))

                    operation = s[i]
                    curNumber = 0
                    i += 1
                 
            if operation == '+': 
                res.append(curNumber)
            elif operation == '-': 
                res.append(-curNumber)
            elif operation == '*': 
                res.append(curNumber * res.pop())
            else: 
                res.append(int(res.pop() / curNumber))
            
            return sum(res)
        
        result = []
        def dfs(num, exp, i, result, target): 
            if i == len(num): 
                if calculate(exp) == target: 
                    result.append(exp)
                return
            
            if exp[-1] != '0':
                dfs(num, exp + num[i], i+1, result, target)
            dfs(num, exp + '+' + num[i], i+1, result, target)
            dfs(num, exp + '-' + num[i], i+1, result, target)
            dfs(num, exp + '*' + num[i], i+1, result, target)
            if num[i] != '0': 
                dfs(num, exp + '/' + num[i], i+1, result, target)
            
        dfs(num, num[0], 1, result, target)
        return result
    
    # 114. Flatten Binary Tree to Linked List
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root == None: 
            return None
        def dfs(node): 
            if node == None: 
                return None
            if node.left == None and node.right == None: 
                return node
            
            leftTail = dfs(node.left)
            rightTail = dfs(node.right)
            if leftTail != None: 
                leftTail.right = node.right
                node.right = node.left
                node.left = None
            if rightTail != None: 
                return rightTail
            else: 
                return leftTail
            
        dfs(root)
        return root
