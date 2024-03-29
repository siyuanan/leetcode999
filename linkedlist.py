class Solution:
    # 206. Reverse Linked List
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # iterative
        # p = None
        # while head != None: 
        #     n = head.next
        #     head.next = p
        #     p = head
        #     head = n
        # return p
        
        # recursive
        # base case
        if head == None or head.next == None: 
            return head
        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead

    # 876. Middle of the Linked List
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p1 = head
        p2 = head
        # return the 1st of the two middle nodes
        # while p2.next != None and p2.next.next != None: 
        #     p1 = p1.next
        #     p2 = p2.next.next
        # return p1
        
        # return the 2nd of the two middle nodes
        while p2!= None and p2.next != None: 
            p1 = p1.next
            p2 = p2.next.next
        return p1
    
    # 141. Linked List Cycle
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: 
            return False
        p1 = head
        p2 = head
        while p2 != None and p2.next != None: 
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2: 
                return True
        return False
    
    # 21. Merge Two Sorted Lists
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        while list1 != None and list2 != None: 
            if list1.val < list2.val: 
                cur.next = list1
                list1 = list1.next
            else: 
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        if list1 != None: 
            cur.next = list1
        else: 
            cur.next = list2
        return dummy.next
    
    # 143. Reorder Linked List
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None or head.next.next == None: 
            return head
        
        # find mid point (1st)
        def mid(head): 
            if head == None or head.next == None: 
                return head
            p1 = head
            p2 = head
            while p2.next != None and p2.next.next != None: 
                p1 = p1.next
                p2 = p2.next.next
            return p1
        
        # reverse the 2nd list
        def reverse(head): 
            if head == None or head.next == None: 
                return head
            p = None
            h = head
            while h != None: 
                n = h.next
                h.next = p
                p = h
                h = n
            return p
        
        def merge(l1, l2): 
            h = ListNode()
            cur = h
            while l1 != None and l2 != None: 
                cur.next = l1
                l1 = l1.next
                cur.next.next = l2
                l2 = l2.next
                cur = cur.next.next
            cur.next = l1
                
        
        mid = mid(head)
        # print(mid.val)
        
        l1 = head
        l2 = mid.next
        # print(l2.val)
        mid.next = None
        l3 = reverse(l2)
        # print(l3.val)
        merge(l1, l3)
        
    # 86. Partition List
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if head == None or head.next == None: 
            return head
        small = ListNode()
        large = ListNode()
        curSmall = small
        curLarge = large
        
        while head != None: 
            if head.val < x: 
                curSmall.next = head
                curSmall = curSmall.next
            else: 
                curLarge.next = head
                curLarge = curLarge.next
            head = head.next
        curSmall.next = large.next
        curLarge.next = None # in case curLarge.next is aonther small node
        return small.next
    
    # 148. merge sort linked list
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head
        # merge sort
        # first divide the list to 2 lists
        def findMid(head): 
            if head == None or head.next == None: 
                return head
            slow = head
            fast = head
            while fast.next != None and fast.next.next != None: 
                slow = slow.next
                fast = fast.next.next
            return slow
        
        mid = findMid(head)
        tail = mid.next
        mid.next = None
        
        # merge 2 sorted list
        def merge(l1, l2): 
            dummy = ListNode()
            cur = dummy
            while l1 != None and l2 != None: 
                if l1.val < l2.val: 
                    cur.next = l1
                    l1 = l1.next
                else: 
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next
            if l1 != None: 
                cur.next = l1
            else: 
                cur.next = l2
            return dummy.next
        
        return merge(self.sortList(head), self.sortList(tail))
    
    # 2. Add Two Numbers
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        x = 0
        while l1 != None or l2 != None or x != 0: 
            if l1 != None: 
                x += l1.val
                l1 = l1.next
            if l2 != None: 
                x += l2.val
                l2 = l2.next
            cur.next = ListNode(val = x % 10)
            cur = cur.next
            x = x // 10
        return dummy.next
    
    # 234. Palindrome Linked List
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None: 
            return True
        # first find the middle node
        slow = head
        fast = head
        while fast.next != None and fast.next.next != None: 
            slow = slow.next
            fast = fast.next.next
        h = slow.next
        slow.next = None
        p = None
        while h != None: 
            n = h.next
            h.next = p
            p = h
            h = n
        while p != None: 
            if head.val != p.val: 
                return False
            else: 
                head = head.next
                p = p.next
        return True
    
    # 203. Remove Linked List Elements
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        while head != None: 
            if head.val == val: 
                p.next = head.next
            else: 
                p = head
            head = head.next
        return dummy.next
            
        
    # 24. Swap Nodes in Pairs
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return None
        if head.next == None: 
            return head
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        while head != None and head.next != None: 
            n = head.next
            head.next = n.next
            n.next = head
            prev.next = n
            
            # prev move to head
            # NOT p.next
            # p.next is the original head.next
            prev = head 
            head = head.next
            
        return dummy.next
    
# 146. LRU Cache
class ListNode: 
    def __init__(self, key, value): 
        self.key = key
        self.val = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.size = 0
        self.cache = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _move_to_head(self, node): 
        # break current link
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1
        # insert after head
        self._add_node(node)
               
    def _add_node(self, node):
        # insert after head
        node.next = self.head.next
        self.head.next = node
        node.next.prev = node
        node.prev = self.head
        self.size += 1
        self.cache[node.key] = node
    
    def _pop_tail(self): 
        self.cache.pop(self.tail.prev.key)
        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev
        self.size -= 1
        
    def get(self, key: int) -> int:
        if key in self.cache: 
            node = self.cache[key]
            self._move_to_head(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache: 
            node = self.cache[key]
            node.val = value
            self._move_to_head(node)
        else: 
            node = ListNode(key = key, value = value)
            self._add_node(node)
            if self.size > self.cap: 
                self._pop_tail()
                
    # 19. Remove Nth Node From End of List
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow = head
        fast = head
        for _ in range(n): 
            fast = fast.next
        if fast == None: 
            return head.next
        
        while fast.next != None: 
            slow = slow.next
            fast = fast.next
            
        slow.next = slow.next.next
        return head

