class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0;i<nums.size();i++){
            for(int j=i+1;j<nums.size();j++){
                int num=nums[i]+nums[j];
                if(num==target){
                    return vector<int>{i,j};
                }
            }
        }
        return vector<int>{0,0};
    }
};