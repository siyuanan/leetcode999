# bfs
class Solution:
    # 314. Binary Tree Vertical Order Traversal
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root == None: 
            return []
        
        q = deque([(root, 0)])
        table = dict()
        min_col = 0
        max_col = 0
        while q: 
            node, col = q.popleft()
            if node != None: 
                min_col = min(col, min_col)
                max_col = max(col, max_col)
                if col not in table.keys(): 
                    table[col] = []
                    
                table[col].append(node.val)
                
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
                
        return [table[c] for c in range(min_col, max_col+1)]
    
    # 339. Nested List Weight Sum
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        q = deque(nestedList)
        s = 0
        d = 1
        while len(q) > 0: 
            for i in range(len(q)): 
                l = q.pop()
                if l.isInteger(): 
                    s += l.getInteger() * d
                else: 
                    # not append
                    # append takes everything as single element
                    # extend put in each element one by one
                    q.extendleft(l.getList())
            d += 1
        return s
    
    # 1091. Shortest Path in Binary Matrix
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
                
        def neighbors(row, col, max_row, max_col, grid): 
            neighbors = []
            for i, j in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]: 
                new_row = row + i
                new_col = col + j
                if new_row >= 0 and new_row <= max_row and new_col >= 0 and new_col <= max_col and grid[new_row][new_col] == 0: 
                    neighbors.append([new_row, new_col])
            return neighbors
        
        max_row = len(grid)-1
        max_col = len(grid[0])-1
        if grid[0][0] == 1 or grid[max_row][max_col] == 1: 
            return -1
        
        # key: current position
        # value: number of node on the path
        visited = {(0,0)}
        q = collections.deque([(0,0,1)])
        q.append([0,0,1])
        while q: 
            cur = q.popleft()
            row = cur[0]
            col = cur[1]
            d = cur[2]
            if row == max_row and col == max_col: 
                return d

            for n in neighbors(row, col, max_row, max_col, grid): 
                if (n[0],n[1]) in visited:  
                    continue
                visited.add((n[0],n[1]))
                q.append([n[0], n[1], d+1])

        return -1
    
    # 199. Binary Tree Right Side View
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root == None: 
            return []
        res = []
        q = collections.deque()
        q.append(root)
        while q: 
            s = len(q)
            for i in range(s): 
                node = q.popleft()
                if node.left != None: 
                    q.append(node.left)
                if node.right != None: 
                    q.append(node.right)
                if i == s-1: 
                    res.append(node.val)
        return res
    
    # 129. Sum Root to Leaf Numbers
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if root == None: 
            return 0
        s = 0
        q = collections.deque()
        q.append((root, 0))
        while q: 
            node, num = q.pop()
            if node.left == None and node.right == None: 
                s += num * 10 + node.val
            if node.left != None: 
                q.append((node.left, num*10 + node.val))
            if node.right != None: 
                q.append((node.right, num*10 + node.val))
        return s
            

