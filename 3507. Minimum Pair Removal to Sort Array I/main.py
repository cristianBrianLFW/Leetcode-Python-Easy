
from typing import List, Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        self.prev = None

class Solution:

    def arrayToList (self, nums: List [ int ]) -> Optional [ ListNode ]:

        if nums:
            head = ListNode(nums[0])
            temp = head

            for i in range ( 1, len ( nums )):
                temp.next = ListNode ( nums [ i ])
                temp.next.prev = temp
                temp = temp.next 

            return head
        return None
    
    def minimunSum ( self, head : Optional[ListNode]) -> Optional[ListNode]:

        if head == None:
            return None
        
        spec = head
        menor = float ("inf")
        keep = None

        while spec and spec.next:
            s = spec.val + spec.next.val
            if s < menor:
                menor = s
                keep = spec
            spec = spec.next

        return keep

    def mergePair ( self, head: Optional [ ListNode], node : Optional [ ListNode]) -> Optional [ListNode]:

        nxt = node.next
        node.val += nxt.val
        node.next = nxt.next

        if node.next:
            node.next.prev = node
        
        return head
    
    def isSorted ( self,  head: ListNode ):

        if not head:
            return False
        
        temp = head

        while temp and temp.next:
            if temp.val > temp.next.val:
                return False
            temp = temp.next

        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:

        head = self.arrayToList(nums)

        ops = 0

        while not self.isSorted(head):

            minumum = self.minimunSum (head)

            self.mergePair(head, minumum)

            ops += 1

        return ops



                            


        
