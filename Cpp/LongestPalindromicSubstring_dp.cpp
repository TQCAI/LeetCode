class Solution {
public:
    string longestPalindrome(string s) {
        int n=s.length();
        int **dp=new int*[n];
        for(int i=0;i<n;i++)
            dp[i]=new int[n];
        if(n==0)
            return "";
        int maxLen=1;
        string ansStr=s.substr(0,1);
        for(int i=0;i<n;i++)
            dp[i][i]=1;
        for(int i=0;i<n-1;i++)
            if(s[i]==s[i+1]){
                dp[i][i+1]=1;
                maxLen=2;
                ansStr=s.substr(i,2);
            }
    
        for(int v=2;v<n;v++){
            for(int i=0;i+v<n;i++){
                int j=i+v;
                if(dp[i+1][j-1]==1 && s[i]==s[j]){
                    dp[i][j]=1;
                    int len=v+1;
                    if(len>maxLen){
                        maxLen=len;
                        ansStr=s.substr(i,len);
                    }
                }
            }
        }
        return ansStr;
    }
};