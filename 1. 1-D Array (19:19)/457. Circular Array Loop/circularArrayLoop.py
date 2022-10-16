#!/usr/bin/env python3
from typing import List

class Solution:
	def circularArrayLoop(self, nums: List[int]) -> bool:
		L = len(nums)
		curr = 0
		tag = 1
		for i in range(L):
			if abs(nums[i]) > 1000:
				continue
			else:
				curr = i
				tag = 1 if nums[curr] > 0 else -1
				while abs(nums[curr]) < 1000*(i+1):
					print(curr, nums)
					next = (curr + tag*(abs(nums[curr])%1000))%L
					if nums[next]*tag < 0:
						break
					
					if next == curr:
						break
					else:
						if abs(nums[next]) > 1000*(i+1):
							return True
						nums[curr] = nums[curr]+1000*(i+1) if nums[curr] > 0 else nums[curr]-1000*(i+1)
						curr = next
						
						
		return False

def main():
	nums = [-1,-1,-1]
	sol = Solution()
	print(sol.circularArrayLoop(nums))
	
if __name__ == "__main__":
	main()