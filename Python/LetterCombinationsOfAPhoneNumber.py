class Solution:
    letter = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    n = 0

    def recursion(self, t):
        if t >= self.n:
            return ['']
        suffixs = self.recursion(t + 1)
        index = self.indexs[t]
        ans = []
        for c in self.letter[index]:
            for suffix in suffixs:
                ans.append(c + suffix)
        return ans

    def letterCombinations(self, digits: str):
        self.n = len(digits)
        self.indexs=list(int(x) for x in digits)
        ans = self.recursion(0)
        if "" in ans:   # 特判
            ans.remove("")
        return ans


ans=Solution().letterCombinations('243')
print(ans)