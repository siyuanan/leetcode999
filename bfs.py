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
