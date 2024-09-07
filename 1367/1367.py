# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def search(self, head: Optional[ListNode], node: Optional[TreeNode]):
        if not head:
            return True
        if not node:
            return False
        if head.val != node.val:
            return False
        return self.search(head.next, node.right) or self.search(head.next, node.left)

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        return self.search(head, root) or self.isSubPath(head, root.left) or self.isSubPath(head, root.right)
        
