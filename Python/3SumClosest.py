class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()
        minAbs = 1<<30
        ans=sum([nums[0], nums[1], nums[-1]])
        n = len(nums)
        for i in range(0, n - 2):
            s = i + 1
            e = n - 1
            while s < e:
                tsum=sum([nums[i], nums[s], nums[e]])
                if abs(target - tsum)<minAbs:
                    minAbs=abs(target - tsum)
                    ans=tsum
                if tsum < target:
                    s += 1
                else:
                    e -= 1
                print()
        return ans


ans = Solution().threeSumClosest([-1, 2, 1, -4], 1)
print(ans)
