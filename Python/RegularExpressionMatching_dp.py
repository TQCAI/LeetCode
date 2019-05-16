class Solution:
    def isMatch(self, text: str, pattern: str) -> bool:
        mem = {}

        def dp(i, j):
            '''
            :return: text[i:] and pattern[j:] is match ?
            '''
            if (i, j) in mem:
                return mem[i, j]
            # if pattern is empty , text must be empty
            if j == len(pattern) :
                return i == len(text)
            first_match = i < len(text) and (pattern[j] in {'.', text[i]})
            if j + 1 < len(pattern) and pattern[j + 1] == '*':
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                ans = first_match and dp(i + 1, j + 1)
            mem[i, j] = ans
            return ans

        return dp(0, 0)


ans = Solution().isMatch('ab', 'a*')
print(ans)
