# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or head.next is None:
            return head
        prev=head
        current=head.next
        while prev != None and current != None:
            current.val, prev.val = prev.val, current.val
            prev = current.next
            current = None if prev == None else prev.next

        return head
        