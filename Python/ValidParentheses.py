class Solution:
    def isValid(self, s: str) -> bool:
        left = '{[('
        right = '}])'
        stack = []
        for i, c in enumerate(s):
            if c in left:
                stack.append(c)
            else:
                judge = len(stack) >= 1 and \
                    left.index(stack[-1]) == right.index(c)
                if not judge:
                    return False
                stack.pop()
        return not len(stack)


ans = Solution().isValid('{[()]}')
print(ans)
