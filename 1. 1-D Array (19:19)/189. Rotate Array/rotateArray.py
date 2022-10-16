#!/usr/bin/env python3
from typing import List

class Solution:
	def rotate(self, nums: List[int], k: int) -> None:
		k = k % len(nums)
		temp = nums[len(nums)-k:len(nums)]
		for i in range(len(nums)-1, k-1, -1):
			nums[i] = nums[i-k]
		for i in range(k):
			nums[i] = temp[i]

def main():
	sol = Solution()
	nums = [1,2]
	sol.rotate(nums, 5)
	print(nums)
	
if __name__ == "__main__":
	main()