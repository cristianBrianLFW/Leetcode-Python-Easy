from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        c = set ()

        while a != None:
            c.add ( a )
            a = a.next

        while b != None:
            if b in c:
                return b
            b = b.next
        
        return None