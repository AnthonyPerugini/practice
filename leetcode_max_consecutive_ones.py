class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_num_ones = 0
        cur_num_ones = 0

        for num in nums:
            if num == 1:
                cur_num_ones += 1
                max_num_ones = max(max_num_ones, cur_num_ones)
            else:
                cur_num_ones = 0


        return max_num_ones

