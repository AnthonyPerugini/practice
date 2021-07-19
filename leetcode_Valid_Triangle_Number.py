from itertools import combinations

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:

        nums_sorted = sorted(nums)

        largest_val = len(nums_sorted) - 1 
        count = 0

        while largest_val >= 2:

            hypotenuse = nums_sorted[largest_val]
            a, b = 0, 1

            # find smallest possible sides, given the hypotenuse.
            while nums_sorted[a] + nums_sorted[b] <= hypotenuse:
                a, b = a + 1, b + 1

            ab_sides_set = len(combinations(nums_sorted[b:largest_val], r=2))
            count += ab_sides_set


            largest_val -= 1

        return count


        
