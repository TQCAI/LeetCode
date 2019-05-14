class Solution:
    def reverse(self, x: int) -> int:
        if not x:
            return 0
        sign=x//abs(x)
        x*=sign
        s=str(x)[::-1]
        x=int(s)
        if x>=(2**31)-1:
            return 0
        return x*sign
    
ans=Solution().reverse(1534236469)
print(ans)