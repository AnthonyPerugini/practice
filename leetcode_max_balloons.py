from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        letter_counter = Counter(text)
        max_count = float('inf')

        for letter in 'balon':
            cur_count = letter_counter[letter]
            
            if letter == 'l' or letter == 'o':
                cur_count //= 2

            max_count = min(max_count, cur_count)

        return max_count
