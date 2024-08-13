# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        previous=head
        current=head.next
        while current:
            if previous.val==current.val:
                if not current.next:
                    previous.next=None
                    break
                current=current.next
                previous.next=current
            else:
                previous=current
                current=current.next
        return head
