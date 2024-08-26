
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        result=[]
        if root is None:
            return result
        s=[root]
        while s:
            current=s.pop()
            result.append(current.val)
            for child in current.children:
                s.append(child)
        result.reverse()
        return result