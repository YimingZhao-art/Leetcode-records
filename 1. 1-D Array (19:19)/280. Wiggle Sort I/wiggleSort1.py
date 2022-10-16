#!/usr/bin/env python3

'''
Given an unsorted array nums, reorder it in-place such that nums[0] < nums[1] > nums[2] < nums[3].... Example:
	
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

from typing import List

class Solution:
	def wiggleSort(self, nums: List[int]) -> None:
		for i in range(len(nums)-1):
			if i % 2 == 0 and nums[i+1] < nums[i]:
				nums[i], nums[i+1] = nums[i+1], nums[i]
			elif i % 2 == 1 and nums[i+1] > nums[i]:
				nums[i], nums[i+1] = nums[i+1], nums[i]

def main():
	sol = Solution()
	nums = [3, 5, 2, 1, 6, 4]
	sol.wiggleSort(nums)
	print(nums)
	
	
if __name__ == "__main__":
	main()