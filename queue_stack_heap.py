# queue & stack & heap
class Solution:
    # 227. Basic Calculator II
    def calculate(self, s: str) -> int:
        if len(s) <= 0: 
            return 0

        stack = deque()
        operation = '-' if s[0] == '-' else '+'
        curNumber = 0

        for i in range(len(s)): 
            # print(f'i: {i}')
            # get the current number
            if s[i] >= '0' and s[i] <= '9': 
                curNumber = 10 * curNumber + int(s[i])

            # reach the next operation
            # finish previous operation
            if (s[i] in ['+', '-', '*', '/']) or (i == len(s)-1): 
                # print(f'si: {s[i]}')
                # print(curNumber)
                if operation == '+': 
                    stack.append(curNumber)
                elif operation == '-': 
                    stack.append(-curNumber)
                elif operation == '*': 
                    stack.append(stack.pop() * curNumber)
                else: 
                    stack.append(int(stack.pop() / curNumber))
                operation = s[i]
                curNumber = 0
                i += 1
                # print(stack)
                # print(operation)      

        res = 0
        while len(stack) > 0: 
            res += stack.pop()
        return res
    
    215. Kth Largest Element in an Array
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def swap(lst, i, j): 
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            
        def percolateDown(lst, i): 
            while i < len(lst) // 2: 
                j1 = i*2+1
                j2 = i*2+2
                if j1 < len(lst) and j2 < len(lst): 
                    if lst[i] > lst[j1]: 
                        if lst[j1] <= lst[j2]: 
                            swap(lst, i, j1)
                            i = j1
                        else: 
                            swap(lst, i, j2)
                            i = j2
                            
                    elif lst[i] > lst[j2]: 
                        if lst[j2] <= lst[j1]: 
                            swap(lst, i, j2)
                            i = j2
                        else: 
                            swap(lst, i, j1)
                            i = j1
                    else: 
                        return
                elif j2 == len(lst): 
                    if lst[i] > lst[j1]: 
                        swap(lst, i, j1)
                        i = j1
                    else: 
                        return
                            
        def percolateUp(lst, i): 
            while i > 0: 
                j = (i-1) // 2
                if lst[j] > lst[i]: 
                    swap(lst, i, j)
                    i = j
                else: 
                    return

                
        # maintain a min heap with k elements
        # new element replace the min(top)
        # then percolate down
        h = nums[:1]
        for n in nums[1:]: 
            # print(h)
            if len(h) < k: 
                h.append(n)
                percolateUp(h, len(h)-1) 
            else: 
                if n > h[0]: 
                    h[0] = n
                    percolateDown(h, 0)
        return h[0]
    
    # 71. Simplify Path
    def simplifyPath(self, path: str) -> str:
        s = []
        for part in path.split('/'): 
            if part == '..': 
                if len(s) > 0: 
                    s.pop()
            elif part == '.' or len(part) <= 0: 
                continue
            else: 
                s.append(part)
        return '/' + '/'.join(s)
    
    
    # 973. K Closest Points to Origin
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # define a comparator
        def closer(p1, p2): 
            return (p1[0]*p1[0] + p1[1]*p1[1]) <= (p2[0]*p2[0] + p2[1]*p2[1])
        
        def swap(q, i, j): 
            tmp = q[i]
            q[i] = q[j]
            q[j] = tmp
        
        # percolat up and down in a max heap
        def percolateUp(q, i): 
            while (i > 0) and (closer(q[(i-1)//2], q[i])): 
                swap(q, i, (i-1)//2)
                i = (i-1)//2
                
        def percolateDown(q, i): 
            while (i < len(q)//2): 
                if i*2+2 >= len(q): 
                    if closer(q[i], q[i*2+1]): 
                        swap(q, i, i*2+1)
                    i = i*2+1

                else: 
                    if (closer(q[i], q[i*2+1]) or closer(q[i], q[i*2+2])): 
                        if closer(q[i*2+1], q[i*2+2]): 
                            swap(q, i, i*2+2)
                            i = i*2+2
                        else: 
                            swap(q, i, i*2+1)
                            i = i*2+1
                    else: 
                        i = len(q)
                    
        res = []
        for p in points: 
            if len(res) < k: 
                res.append(p)
                percolateUp(res, len(res)-1)
            else: 
                if closer(p, res[0]): 
                    res[0] = p
                    percolateDown(res, 0)
                    
        return res
    
    # 347. Top K Frequent Elements
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # record number and counts
        num_dict = {}
        for n in nums: 
            if n in num_dict: 
                num_dict[n] += 1
            else: 
                num_dict[n] = 1
        
        def swap(lst, i, j): 
            tmp = lst[i]
            lst[i] = lst[j]
            lst[j] = tmp
            
        # compare needs to use <=
        # in case i > j1 = j2
        def compare(lst, i, j, num_dict): 
            return num_dict[lst[i]] <= num_dict[lst[j]]
        
        # use mean heap to store k elements
        # if new elements > top, replace top then percolate down
        def percolateUp(lst, i, num_dict): 
            while i > 0: 
                j = (i-1) // 2
                if compare(lst, i, j, num_dict): 
                    swap(lst, i, j)
                    i = j
                else: 
                    break
        def percolateDown(lst, i, num_dict): 
            while i < len(lst)//2: 
                j1 = i*2+1
                j2 = i*2+2
                if j2 == len(lst): # only 1 child
                    if compare(lst, j1, i, num_dict): 
                        swap(lst, i, j1)
                        i = j1
                    else: 
                        i = len(lst)
                else: # 2 children
                    if compare(lst, j2, j1, num_dict) and compare(lst, j2, i, num_dict):
                        swap(lst, i, j2)
                        i = j2
                    elif compare(lst, j1, j2, num_dict) and compare(lst, j1, i, num_dict):
                        swap(lst, i, j1)
                        i = j1
                    else: 
                        i = len(lst)

        res = []
        for n in num_dict: 
            if len(res) < k: 
                res.append(n)
                percolateUp(res, len(res)-1, num_dict)
            else: 
                if num_dict[res[0]] < num_dict[n]: 
                    res[0] = n
                    percolateDown(res, 0, num_dict)
        return res
    
    # 23. Merge k Sorted Lists
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0: 
            return None
        if len(lists) == 1: 
            return lists[0]
        
        def swap(q, i, j): 
            tmp = q[i]
            q[i] = q[j]
            q[j] = tmp
            
        def percolateUp(q, i): 
            # i small, i move up
            while i > 0: 
                j = (i - 1) // 2
                if q[i].val < q[j].val: 
                    swap(q, i, j)
                    i = j
                else: 
                    break
                    
        def percolateDown(q, i): 
            # i large, i move down
            while i < len(q) // 2:
                j1 = i * 2 + 1
                j2 = i * 2 + 2
                if j2 < len(q): # both children exist
                    if q[i].val > q[j1].val or q[i].val > q[j2].val:  # swap
                        if q[j1].val > q[j2].val: 
                            swap(q, i, j2)
                            i = j2
                        else: 
                            swap(q, i, j1)
                            i = j1
                    else: 
                        break
                else: # only j1
                    if q[i].val > q[j1].val: 
                        swap(q, i, j1)
                        i = j1
                    else: 
                        break

        dummy = ListNode()
        cur = dummy
        # use min heap with k elements to store nodes
        q = []
        for l in lists: 
            if l != None: 
                q.append(l)
                percolateUp(q, len(q)-1)
        
        if len(q) == 0: 
            return None
        if len(q) == 1: 
            return q[0]
        
        while len(q) > 1: 
            node = q[0]
            next_node = node.next
            if next_node == None: # this list is finished
                next_node = q.pop()
            q[0] = next_node
            percolateDown(q, 0)
            cur.next = node
            cur = cur.next
            
        cur.next = q[0]
        return dummy.next
                
        
        
                
                
                
                
                
                
