#!/usr/bin/env python3
from typing import List

class Solution:
	def twoSum(self, nums: List[int], target: int, left: int, right: int):
		List = []
#		print("twosum", "target:", target, nums)
		while left < right:
#			print(nums[left], nums[right], target)
			sumOfTwo = nums[left] + nums[right]
			if sumOfTwo == target:
				List.append([nums[left], nums[right]])
				while left < right and nums[left] == nums[left+1]:
					left += 1
				left += 1
				while left < right and nums[right] == nums[right-1]:
					right -= 1
				right -= 1
			elif sumOfTwo < target:
				left += 1
			else:
				right -= 1
				
		return List
	
	def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
		k = len(nums)-1
		List = []
#		print("threesum", "target:", target, nums)
		
		for i in range(k-1):
			# print(target)
			if i > 0 and nums[i] == nums[i-1]:
				continue
			L = self.twoSum(nums, target-nums[i], i+1, k)
			if  L != []:
				for each in L:
					each.append(nums[i])
					each.sort()
					List.append(each)
		return List
	
	def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
		nums.sort()
		List = []
#		print(nums)
		for i in range(len(nums)-3):
			if i > 0 and nums[i] == nums[i-1]:
				continue
			L = self.threeSum(nums[i+1:], target-nums[i])
			if L != []:
				for each in L:
					each.append(nums[i])
					each.sort()
					List.append(each)
		
		return List


sol = Solution()
a = sol.fourSum([1,0,-1,0,-2,2], 0)
print(a)