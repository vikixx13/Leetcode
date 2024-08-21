# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        s=[]
        result=[]
        current=root
        while current or s:
            while current:
                s.append(current)
                current=current.left
            current=s.pop()
            result.append(current.val)
            current=current.right
        return result


        
        