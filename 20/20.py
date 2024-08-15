class Solution(object):
    def isValid(self, s):
        stack = []
        brackets= {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        for b in s:
            if b in brackets:
                stack.append(b)
            elif len(stack) == 0 or b != brackets[stack.pop()]:
                return False

        return len(stack) == 0