#!/usr/bin/env python3

'''
Given an unsorted array nums, reorder it in-place such that nums[0] < nums[1] > nums[2] < nums[3].... Example:
	
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

from typing import List

class Solution:
	def wiggleSort(self, nums: List[int]) -> None:
		nums.sort()
		nums1 = nums[:]
		
		j = int((len(nums)-1)/2)
		k = len(nums)-1
		jj = j
		i = 0
		while i < len(nums)-1:
			if j > -1:
				nums[i] = nums1[j]
				i += 1
				j -= 1
			if k > jj:
				nums[i] = nums1[k]
				i += 1
				k -= 1
		
		
def main():
	sol = Solution()
	nums = [1,4,2,4,4,6]
	
	
	sol.wiggleSort(nums)
	print(nums)
	
	
if __name__ == "__main__":
	main()