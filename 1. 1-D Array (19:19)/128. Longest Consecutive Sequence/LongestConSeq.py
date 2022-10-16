#!/usr/bin/env python3
from typing import List

class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		hashMap = {}
		for each in nums:
			if each in hashMap:
				continue
			else:
				if (not each-1 in hashMap) and (not each+1 in hashMap):
					hashMap[each] = 1
				else:
					if (not each-1 in hashMap) and (each+1 in hashMap):
						hashMap[each] = hashMap[each+1]
						while each in hashMap:
							hashMap[each] += 1
							each += 1
					elif (each-1 in hashMap) and (not each+1 in hashMap):
						hashMap[each] = hashMap[each-1]
						while each in hashMap:
							hashMap[each] += 1
							each -= 1
					else:
						hashMap[each] = hashMap[each+1] + hashMap[each-1] + 1
						i, j = each-1, each+1
						while i in hashMap:
							hashMap[i] = hashMap[each]
							i -= 1
						while j in hashMap:
							hashMap[j] = hashMap[each]
							j += 1
		maxl = 0
		for each in hashMap:
			maxl = max(maxl,hashMap[each])
							
		return maxl
						
					

def main():
	sol = Solution()
	print(sol.longestConsecutive([100,4,200,1,3,2]))
	
if __name__ == "__main__":
	main()