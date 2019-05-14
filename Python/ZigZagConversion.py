class Solution:
    def convert(self, s: str, numRows: int) -> str:
        lines=['']*numRows
        index=0
        n=len(s)
        try:
            while index<n:
                # vertical
                for i in range(numRows):
                    lines[i]+=s[index]
                    index+=1
                    if index>=n:
                        raise Exception
                for i in range(numRows-2):
                    target=numRows-i-2
                    for j in range(numRows):
                        if j==target:
                            lines[j] += s[index]
                            index += 1
                        else:
                            lines[j] += ' '
                        if index >= n:
                            raise Exception
        except Exception:
            pass
        # print(*lines,sep='\n')
        ans=''
        for line in lines:
            for c in line:
                if c!=' ':
                    ans+=c
        return ans



Solution().convert('LEETCODEISHIRINGB',4)

