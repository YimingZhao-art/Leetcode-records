#!/usr/bin/env python3
from typing import List

class Solution:
	def findDuplicates(self, nums: List[int]) -> List[int]:
		L = []
		for each in nums:
			if nums[abs(each)-1] < 0:
				L.append(abs(each))
			else:
				nums[abs(each)-1] *= -1
		return L
	
	
def main():
	
	
if __name__ == "__main__":
	main()