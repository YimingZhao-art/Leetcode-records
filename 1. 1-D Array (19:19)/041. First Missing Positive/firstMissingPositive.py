#!/usr/bin/env python3
from typing import List

class Solution:
	def firstMissingPositive(self, nums: List[int]) -> int:
		l = len(nums)
		for i in range(l):
			while nums[i] > 0 and nums[i] <= l and nums[i] != nums[nums[i]-1]:
				temp = nums[nums[i]-1]
				nums[nums[i]-1] = nums[i]
				nums[i] = temp
		for i in range(l):
			if nums[i] != i+1:
				return i+1
		return l+1
	
		
def main():
	nums = [3,4,-1,1]
	sol = Solution()
	print(sol.firstMissingPositive(nums))
	
if __name__ == "__main__":
	main()