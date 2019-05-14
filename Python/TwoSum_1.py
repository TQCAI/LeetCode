class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        reference: https://leetcode.com/problems/two-sum/discuss/17/Here-is-a-Python-solution-in-O(n)-time
        '''
        buff_dict = {}
        for i in range(len(nums)):
            cur = nums[i]  # current number
            if cur in buff_dict:
                return [buff_dict[cur], i]
            else:
                buff_dict[target - cur] = i
        raise AttributeError("No solution")
