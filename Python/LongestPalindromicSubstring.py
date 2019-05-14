class Solution:
    def longestPalindrome(self, s: str) -> str:
        from copy import deepcopy
        if s == "":
            return ""
        n = len(s)
        dp = [[0 for i in range(n)] for j in range(n)]
        max_len = 1
        ans_str = s[0]
        for i in range(n):
            dp[i][i] = 1
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = 1
                max_len = 2
                ans_str = s[i:i + 2]
        for v in range(2, n):
            for i in range(n - v):
                j = i + v
                if s[i] == s[j] and dp[i + 1][j - 1] == 1:
                    dp[i][j] = 1
                    if v + 1 > max_len:
                        max_len = v + 1
                        ans_str = s[i:j + 1]
        return ans_str


if __name__ == '__main__':
    ans=Solution().longestPalindrome("abcda")
    print(ans)