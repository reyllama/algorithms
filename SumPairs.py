def sum_pairs(ints, s):
	if len(ints) <= 1:
		return None
	for i in range(1, 2*len(ints)):
		nums = [[ints[j], ints[i-j]] for j in range(int((i+1)/2)) if i-j in range(0, len(ints))]
		print(i, nums)
		for num in nums[::-1]:
			if sum(num) == s:
				return num
	return None

def sum_pairs(ints, s):
	if len(ints) <= 1:
		return None
	memo = []
	for i in range(len(ints), 1, -1):
		for j in range(i-2, -1, -1):
			if ints[i-1] + ints[j] == s:
				memo.append([ints[j], ints[i-1]])
	if len(memo)<1:
		return None
	return memo[-1]

def sum_pairs(ints, s):
	for i in range(1, len(ints)):
		print(i)
		for j in range(0, i):
			if ints[i] + ints[j] == s:
				return [ints[j], ints[i]]

def sum_pairs(ints, s):
	nums = sorted(ints)
	print(nums)
	memo = []
	for i in range(1, len(ints)):
		if nums[i] < s/2:
			continue
		for j in range(i-1, -1, -1):
			if nums[i] + nums[j] == s:
				return [nums[j], nums[i]] if ints.index(nums[j]) < ints.index(nums[i]) else [nums[i], nums[j]]

def sum_pairs(ints, s):
	for i in range(1, len(ints)):
		nums = sorted(ints[:i])
		if nums[int(len(nums)/2)] + ints[i] < s:
			for j in range(int(len(nums)/2)+1, len(nums)):
				if nums[j] + ints[i] == s:
					return [nums[j], ints[i]]

def sum_pairs(ints, s):
	for i in range(1, len(ints)):
		print(i)
		if s-ints[i] in ints[:i]:
			return [ints[ints[:i].index(s-ints[i])], ints[i]]

def sum_pairs(lst, s):
    cache = set()
    for i in lst:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


l0 = list(range(100000))
l1= [1, 4, 8, 7, 3, 15] # 8
l2= [1, -2, 3, 0, -6, 1] # -6
l3= [20, -13, 40] #-7
l4= [1, 2, 3, 4, 1, 0] #2
l5= [10, 5, 2, 3, 7, 5] #10
l6= [4, -2, 3, 3, 4] #8
l7= [0, 2, 0] #0
l8= [5, 9, 13, -3] #10

import time

t0 = time.time()
print(sum_pairs(l0, 100000))
print("Time spent: {:.3f}".format(time.time()-t0))
# print(list(l0))
# print(l0)
