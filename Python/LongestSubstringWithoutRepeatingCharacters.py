class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        sub_str = ""
        for c in s:
            if c in sub_str:
                pos = sub_str.find(c)
                sub_str = sub_str[pos + 1:]
                sub_str += c
            else:
                sub_str += c
            max_len = max(max_len, len(sub_str))
        return max_len
