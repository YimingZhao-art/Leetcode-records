#!/usr/bin/env python3

'''
Given an unsorted array nums, reorder it in-place such that nums[0] < nums[1] > nums[2] < nums[3].... Example:
	
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
'''

from typing import List

class Solution:
	def convert(self, i : int, n: int) -> int:
		if n % 2 == 0:
			n += 1
		return (2*i+1) % n
	
	def wiggleSort(self, nums: List[int]) -> None:
		n = len(nums)
		_ = sorted(nums)
		mid = _[int(n/2)]
		
		i,j,k = 0,0,n-1

		while j <= k:
			if nums[self.convert(j, n)] > mid:
				nums[self.convert(j, n)], nums[self.convert(i, n)] = nums[self.convert(i, n)], nums[self.convert(j, n)]
				i += 1
				j += 1
			elif nums[self.convert(j, n)] < mid:
				nums[self.convert(j, n)], nums[self.convert(k, n)] = nums[self.convert(k, n)], nums[self.convert(j, n)]
				k -= 1
			else:
				j += 1
				
def main():
	sol = Solution()
	nums = [1,1,1,3,4,5]
	
	
	sol.wiggleSort(nums)
	print(nums)
	
	
if __name__ == "__main__":
	main()