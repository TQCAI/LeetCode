package TwoSum;

import java.util.HashMap;

public class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashMap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int cur = nums[i];
            if (hashMap.containsKey(cur)) {
                return new int[] { hashMap.get(cur), i };
            } else {
                hashMap.put(target - cur, i);

            }
        }
        throw new IllegalArgumentException("No solution");

    }
}