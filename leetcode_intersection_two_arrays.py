from collections import defaultdict

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1 = defaultdict(int)
        res = []

        for num in nums1:
            n1[num] += 1

        for num in nums2:
            if n1[num]:
                res.append(num)
                n1[num] -= 1

        return res

