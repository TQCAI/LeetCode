class Solution {
public:
    string longestPalindrome(string s) {
        int dp[1010][1010]={0};
        int n=s.length();
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
                
        for(int i=0;i<n;i++){
            for(int v=2,j=i+v;j<n;v++){
                if(dp[i+1][j-1]==1 && s[i]==s[j]){
                    dp[i][j]=1;
                    if(v>maxLen){
                        maxLen=v;
                        ansStr=s.substr(i,v);
                    }
                }
            }
        }
        return ansStr;
    }
};