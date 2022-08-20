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
