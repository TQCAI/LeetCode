class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        sign=1
        if not s:
            return 0
        if s[0]== '-':
            sign=-1
            s= s[1:]
        elif s[0]=='+':
            sign=1
            s= s[1:]
        obj=''
        for c in s:
            if c.isdigit():
                obj+=c
            else:
                break
        if not obj:
            return 0
        ans=int(obj)*sign
        ans=max(-2**31,ans)
        ans=min(2**31-1,ans)
        return ans
