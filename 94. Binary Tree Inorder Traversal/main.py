from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        self.simetrica(root, a)
        return a
    def simetrica ( self, node: Optional[TreeNode], resultado : List):

        if node is None:
            return None
        
        self.simetrica ( node.left, resultado)
        resultado.append(node.val)
        self.simetrica( node.right, resultado)

        

