#arr = [4,5,5,5,6,10]	
arr = [1,2,2,3,3,4]

def find_max_index(arr: list, target: int) -> int:
	"""
	return the index of the right-most position that we can insert target into the sorted arr
	"""
	if not len(arr):
		return -1

	lo = 0
	hi = len(arr)
	while lo < hi:
		mid = lo + (hi-lo)//2
		if arr[mid] > target:
			hi = mid
		else:
			lo = mid + 1
	
	return lo if lo !=0 and arr[lo-1] == target else -1


def find_min_index(arr: list, target: int) -> int:
	"""
	return the index of the left-most position that we can insert target into the sorted arr
	"""
	if not len(arr):
		return -1

	lo = 0
	hi = len(arr)
	while lo < hi:
		mid = lo + (hi-lo)//2 
		if arr[mid] >= target:
			hi = mid
		else:
			lo = mid + 1
	return lo if arr[lo] == target else -1


def find_min_or_max_index(arr: list, target: int, searchtype='min') -> int:
	"""
	return the min or max index of a given target value in a sorted arr.
	returns -1 if the element doesn't exist.
	"""
	if not len(arr):
		return -1

	if searchtype not in {'min','max'}:
		raise ValueError("searchtype must be 'min' or 'max'")

	# this one function 'hack' only works for ints.  the += must be equal to the smallest increment that can
	# seperate values.  (e.g 0.25 to seperate values that vary by +/- 0.25 [2, 2.25] [5.5, 5.75]
	if searchtype == 'max':
		target += 1
		
	lo = 0
	hi = len(arr)

	while lo < hi:
		mid = lo + (hi-lo)//2

		if arr[mid] >= target:
			hi = mid
		else:
			lo = mid + 1

	if searchtype == 'max':
		return lo if lo < len(arr) + 1 else -1
	if searchtype == 'min':
		return lo if arr[lo] == target else -1


def count_repeats(arr, target):
	min_index = find_min_or_max_index(arr, 4, searchtype='min')
	if min_index == -1:
		return -1

	max_index = find_min_or_max_index(arr, 4, searchtype='max')
	return max_index - min_index

print(count_repeats(arr, 4))
