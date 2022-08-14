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
            
