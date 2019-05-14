#include <bits/stdc++.h> 
#define FF(a,b) for(int a=0;a<b;a++) 
#define F(a,b) for(int a=1;a<=b;a++) 
#define LEN 200 
#define INF 100000 
#define bug(x) cout<<#x<<"="<<x<<endl; 

using namespace std; 
typedef long long ll; 
const double pi=acos(-1);

string convert(string s, int numRows){
	// 一波操作
	string *row =new string[numRows];
	int pos=0;
	int n=s.length();
	int curCol=1;
	int i=0;
	while(i<n){// 全局索引 
		for(int j=0;j<numRows && i<n;j++){ //当前行号 
			row[j]+=s[i++];
			row[j]+=' ';
		}
		if(i+1<n){
			int mid=numRows/2;
			row[mid][curCol]=s[i++];
			curCol+=2;
		}
	}
	string ans;
	for(int i=0;i<numRows;i++)
		bug(row[i])
	for(int r=0;r<numRows;r++){
		for(int c=0;c<curCol;c++){
			if(row[r][c]!=' '){
				ans+=row[r][c]; 
			}
		}
	}
	return ans;
}


int main(){
//	freopen("")
	string ans=convert("PAYPALISHIRING",4);
	bug(ans)
	return 0;
}

