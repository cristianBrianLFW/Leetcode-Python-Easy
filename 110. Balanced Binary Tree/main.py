from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# criar uma funcao que retorna a altura de uma árvore com base da raiz

# pegar o valor do sub Arvore a esquerda e a direita, calcular o módulo, se for maior que menor ou igual a 1 retorna true,

# se não retorna 0

class Solution:

    def isTreeHeight (self, root : Optional [ TreeNode ]) -> int:

        if root != None:

            hl = self.isTreeHeight ( root.left )
            hr = self.isTreeHeight ( root.right )

            if hl > hr:
                return hl + 1
            else:
                return hr + 1 

        return 0
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if root != None:

            hl = self.isTreeHeight ( root.left )

            hr = self.isTreeHeight ( root.right )

            if abs ( hl - hr ) <= 1:

                l = self.isBalanced ( root.left )

                r = self.isBalanced ( root.right )

                return True and l and r
            else:

                return False

        return True
    


a = TreeNode (3)

b = TreeNode (9)

c = TreeNode (15)

d = TreeNode (20)

e = TreeNode (7)

a.left = b

a.right = d

d.left = c

d.right = e

# f = TreeNode(12)

# e.left = f


s = Solution()

print ( s.isBalanced(a))



        

        