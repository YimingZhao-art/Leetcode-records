#!/usr/bin/env python3
from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		nums = set(nums)
		longest = 0
		
		
		for each in nums:
			if each-1 not in nums:
				current_num = each
				current_length = 1
				
				while current_num+1 in nums:
					current_length += 1
					current_num = current_num+1
				
				longest = max(longest, current_length)
		return longest
					

def main():
	sol = Solution()
	print(sol.longestConsecutive([100,4,200,1,3,2]))
	
if __name__ == "__main__":
	main()