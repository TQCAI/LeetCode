class Solution:

    def generateParenthesis(self, n: int) -> list:
        ans = []

        def dfs(s: str, left: int, right: int):
            if left+right == n*2:
                ans.append(s)
            if left < n:
                dfs(s+'(', left+1, right)
            if right < left:
                dfs(s+')', left, right+1)
        dfs('', 0, 0)
        return ans

ans = Solution().generateParenthesis(4)
# expected = ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()",
#             "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]
# diff = set(expected)-set(ans)
# print(diff)

print(ans)
