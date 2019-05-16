class Solution {
public:
int maxArea(vector<int>& height) {
	int n=height.size();
	int a=0,b=n-1;
	int maxVolume=0;
	while(a<b){
		int volume=(b-a)*min(height[a],height[b]);
		maxVolume=max(volume,maxVolume);
		if(height[a]<height[b])
			a++;
		else 
			b--;
	}
	return maxVolume;
}
};