from collections import defaultdict

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        comps = defaultdict(int)

        for i, num in enumerate(nums):
            comp = target - num

            if comp in comps:
                return comps[comp], i
            else:
                comps[num] = i

        return False

