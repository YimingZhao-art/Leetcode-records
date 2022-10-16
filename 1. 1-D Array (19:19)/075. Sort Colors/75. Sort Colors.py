#!/usr/bin/env python3
from typing import List

class Solution:
	def sortColors(self, nums: List[int]) -> None:
		#i is the firt non-zero, j is the first non-two
		l = len(nums)
		low = 0
		mid = 0
		high = l-1
		while mid <= high:
			if nums[mid] == 0:
				nums[mid], nums[low] = nums[low], nums[mid]
				mid += 1
				low += 1
			elif nums[mid] == 1:
				mid += 1
			else:
				nums[mid], nums[high] = nums[high], nums[mid]
				high -= 1

		

