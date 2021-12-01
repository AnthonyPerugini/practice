class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.shuffled = self.nums[:]        

    def reset(self) -> List[int]:
        self.shuffled = self.nums[:]
        """
        Resets the array to its original configuration and return it.
        """
        return self.shuffled
        
    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        from random import shuffle
        shuffle(self.shuffled)
        return self.shuffledlass Solution:


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
