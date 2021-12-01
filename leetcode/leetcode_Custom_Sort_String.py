from collections import Counter

class Solution:
    def customSortString(self, order: str, str: str) -> str:

        letter_counter = Counter(str)
        ret = []

        for letter in order:
            if letter in letter_counter:
                count = letter_counter.pop(letter)
                ret.extend(letter*count)

        while letter_counter:
            letter, count = letter_counter.popitem()
            ret.extend(letter*count)

        return ''.join(ret)



