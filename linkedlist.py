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
            
