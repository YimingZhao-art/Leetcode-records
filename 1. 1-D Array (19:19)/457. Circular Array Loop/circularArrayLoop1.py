#!/usr/bin/env python3
from typing import List

class Solution:
	def circularArrayLoop(self, nums: List[int]) -> bool:
		length = len(nums)
		tag = 1
		
		def getNext(index):
			if nums[index]*tag > 0:
				next = (nums[index]+index)%length
				return next if next != index else -1
			return -1
			
		for i in range(length):
			slow = fast = i
			tag = -1 if nums[i] < 0 else 1
			while True:
				slow = getNext(slow)
				if slow == -1:
					break
				for _ in range(2):
					fast = getNext(fast)
					if fast == -1:
						break
				if slow == fast:
					return True
		
		return False
	
def main():
	nums = [6]
	sol = Solution()
	print(sol.circularArrayLoop(nums))
	
	
if __name__ == "__main__":
	main()