# bfs
class Solution:
    # 314. Binary Tree Vertical Order Traversal
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque([(root, 0)])
        table = dict()
        while q: 
            node, col = q.popleft()
            if node != None: 
                if col not in table.keys(): 
                    table[col] = []
                    
                table[col].append(node.val)
                
                q.append((node.left, col - 1))
                q.append((node.right, col + 1))
                
        return [table[c] for c in sorted(table.keys())]
