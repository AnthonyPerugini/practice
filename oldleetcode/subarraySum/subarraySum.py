#! /home/anthony/miniconda3/envs/fun/bin/python

def subarraySum(lst: list[int], target: int) -> int:
    sum_arr = [0]
    
    sub_sum = 0
    for num in lst:
        sub_sum += num
        sum_arr.append(sub_sum)
    
    lo = 0
    hi = 0
    count = 0
    idx_arr = []
    while hi < len(sum_arr)-1:
        if lo > hi:
            hi += 1
            continue
        sub_total = sum_arr[hi+1] - sum_arr[lo] 
        if sub_total == target:
            count += 1
            idx_arr.append((lo, hi))
            lo += 1
        elif sub_total < target:
            hi += 1
        else:
            lo += 1
    print(sum_arr)
    return count, idx_arr

arr = [1,2,3,4,5,6,7]
print(subarraySum(arr, 1))
