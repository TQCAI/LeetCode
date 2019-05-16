import itertools
import collections


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        counter = collections.Counter(nums)
        numbers = list(x for x in counter.keys())
        pairs = itertools.combinations(numbers, 2)
        ans = set()
        for a, b in pairs:
            c = -a - b
            if (c in counter) and (len({a, b, c}) == 3 or counter[c] > 1):
                ans.add(tuple(sorted([a, b, c])))
        if counter[0]>=3:
            ans.add((0,0,0))
        return [list(x) for x in ans]
