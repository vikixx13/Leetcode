# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def gcd(self, x: int, y: int) -> int:
        while y != 0:
                x, y = y, x % y
        return x
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next:
            return head
        
        first = head
        second = head.next

        while second:
            gvalue = self.gcd(first.val,second.val)
            gnode=ListNode(gvalue)
            first.next = gnode
            gnode.next = second
            first = second
            second = second.next

        return head