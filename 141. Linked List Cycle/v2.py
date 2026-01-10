from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        fast, slow = head, head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next
            fast = fast.next
            
            if ( slow == fast ):
                return True
            
        return False

s = Solution()

# nodes = int (input ("Digite quantos nós tem sua lista : "))

# if ( nodes > 0 ):
#     valor = int ( input (f"Digite o valor do nó {1}: ") )
#     head = ListNode ( valor )
#     head.next = None
#     temp = head
#     for i in range ( 1, nodes ):
#         valor = int ( input (f"Digite o valor do nó {i + 1}: ") )
#         temp.next = ListNode ( valor )
#         temp = temp.next
# else:
#     print ( "lista de nós vazia")

head = ListNode (3)

no1 = ListNode ( 2 )

no2 = ListNode ( 0 )

no3 = ListNode ( 4 )

head.next = no1

no1.next = no2

no2.next = no3

no3.next = no2

print ( s.hasCycle(head))
