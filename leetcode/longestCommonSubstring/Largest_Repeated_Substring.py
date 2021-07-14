
# seperators used for concatenating the strings together
# can be anything, as long as they are lexcographically < [a-z, A-Z]
SENTINALS = '!@#$%^&*()_+;'

S1 = 'AABC'
S2 = 'BCDC'
S3 = 'BCDE'
S4 = 'CDED'
# Minimum number of strings that are required to share the substring. Given in problem definition.
K = 2

def LCP(word1: str, word2: str) -> int:
    """
    Returns:
        int: Length of the largest prefix shared between two strings.
    """
    count = 0
    for letter1, letter2 in zip(word1, word2):
        if letter1 != letter2:
            break
        count += 1
    return count

def sentinal_group(string: str, sentinals: str) -> int:
    """
    Returns:
        int: Group that the suffix originated in (s0, s1, ...)
    """
    for char in string:
        if char in sentinals:
            return sentinals.index(char)

def concatenate_with_sentinals(*strings: list[str], sentinals: str) -> str:
    """
    Raises:
        ValueError: If there are more terms than sentinals, a unique sentinal 
        cannot seperate each term, and the algorithm will fail.

    Returns:
        str: Concatenated version of the strings, with unique sentinals seperating each string.
    """
    if len(strings) > len(sentinals):
        print("Can't handle that many terms.  Add more sentinals to the 'sentinals' variable")
        raise ValueError

    ret = []
    for string in strings:
        new_string = string[:] + sentinals[0]
        sentinals = sentinals[1:]
        ret.append(new_string)

    return ''.join(ret)

def num_unique_groups(groups: list[int]) -> int:
    """
    Returns:
        int: Returns the number of unique groups found in the list of groups provided.
    """
    seen = set()
    count = 0
    for group_num in groups:
        if group_num not in seen:
            count += 1
            seen.add(group_num)
    return count
    """Finds the last element in the current window that has the max_lcp value.  This is garunteed to
       be the longest substring.
    
    Returns:
        str: Longest shared prefix in the provided window
    """
    for lcp, suffix in window[::-1]:
        if lcp == max_lcp:
            return suffix


concatenated_strings = concatenate_with_sentinals(S1, S2, S3, S4, sentinals=SENTINALS)


# build the sorted suffix table, remove elements that start with a sentinal value
# currently O(nlogn). this can be done in O(n) but im not smart enough.
# TODO: implement the algorithm to do this in O(n) time (https://www.geeksforgeeks.org/suffix-array-set-2-a-nlognlogn-algorithm/)
suffixes = []
for i in range(len(concatenated_strings) - 1, -1, -1):
    if concatenated_strings[i:][0] not in (SENTINALS):
        suffixes.append(concatenated_strings[i:])
suffixes_sorted = sorted(suffixes)

# element i in the lcp_array corresponds to the length of the shared prefix between suffix at position i and i-1
# suffix group_num is the original group_num that the suffix belonged to (S1 -> group 0, S2 -> group 1, ...)
lcp_array = [0] * len(suffixes_sorted)
suffix_group = {}
for i in range(0, len(suffixes_sorted)):
    suffix = suffixes_sorted[i]
    if i != 0:
        common_letters = LCP(suffixes_sorted[i-1], suffixes_sorted[i])
        lcp_array[i] = common_letters
    suffix_group[suffix] = sentinal_group(suffix, SENTINALS)

# print(len(suffixes_sorted))
# print(len(lcp_array))
# print(len(suffix_group))



# use a sliding window of variable size (hi - lo) across the lcp_suffix_table.
lo = 0
hi = K
longest_common_substrings = set()
longest_common_substrings_length = 0

lcp_suffix_table = [ele for ele in zip(lcp_array, suffixes_sorted)]

# terminate when hi reaches the end of the table and we don't have enough groups captured
while hi < len(suffixes_sorted):

    window = lcp_suffix_table[lo:hi]
    window_groups = [suffix_group[suffix] for _, suffix in window]
    # print(f'window: {window}')
    # print(f'groups: {window_groups}')

    # not enough groups caught in window, expand the window and try again
    if num_unique_groups(window_groups) < K:
        hi += 1
        # print('not enough groups caught, expanding window')
        continue

    # we ignore lcp for the first element (would give us lcp for lo and lo-1)
    max_lcp, suffix = min([(lcp, suffix) for lcp, suffix in window[1:]], key=lambda x: x[0]) if window[1:] else 0
    # print(f'max_lcp and suffix: {max_lcp}, {suffix}')


    # prefix tied for longest substring.  add to list
    if max_lcp == longest_common_substrings_length and max_lcp > 0:
        longest_common_substrings.add(suffix[:max_lcp])
        # print('found a substring tied for longest')
        # print(f'{longest_common_substrings}')  

    # new longest substring found, clear old list, append suffix to new list, and update max   
    if max_lcp > longest_common_substrings_length:
        longest_common_substrings = set()
        longest_common_substrings.add(suffix[:max_lcp])
        longest_common_substrings_length = max_lcp
        # print('found a new longest substring')
        # print(f'{longest_common_substrings}')

    # k or more groups were in the window, contract the window
    lo += 1
    # print('contracting window')

print(longest_common_substrings)