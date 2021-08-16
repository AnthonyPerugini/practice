class NumArray:

    def __init__(self, nums: List[int]):
        self.nums_sum = self.num_sum(nums)

    def sumRange(self, left: int, right: int) -> int:
        
        return self.nums_sum[right] if left == 0 else self.nums_sum[right] - self.nums_sum[left-1]


    def num_sum(self, nums):
        nums_sum = []
        total = 0
        for num in nums:
            total += num
            nums_sum.append(total)

        return nums_sum
