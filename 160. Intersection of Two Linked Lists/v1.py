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

        while a != None or b != None:
            if a != None:
                if a in c:
                    return a
                else:
                    c.add ( a )
                    a = a.next
            if b != None:
                if b in c:
                    return b
                else:
                    c.add ( b )
                    b = b.next
        return None
