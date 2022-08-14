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
