class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int,int> hashMap;
        for(int i=0;i<nums.size();i++){
            int cur=nums[i];
            if(hashMap.count(cur)){
                return vector<int>{i,hashMap[cur]};
            }else{
                hashMap[target-cur]=i;
            }
        }
        return vector<int>{0,0};
    }
};