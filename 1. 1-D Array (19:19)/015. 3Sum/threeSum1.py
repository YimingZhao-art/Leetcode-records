from typing import List

class Solution:
	"""
	O(n^2)
	"""
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		dictHashmap = dict()
		List = []
		for i in range(len(nums)):
			dictHashmap[nums[i]] = i
		for i in range(len(nums)): 
			if target-nums[i] in dictHashmap and i!=dictHashmap[target-nums[i]]:
				List.append([nums[i], target-nums[i]])
		return List
	
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		i, j, k = 0, 1, len(nums)-1
		List = []
		while i < j and j < k:
			target = 0-nums[k]
			# print(target)
			L = self.twoSum(nums[:k], target)
			if  L != []:
				for each in L:
					each.append(nums[k])
					each.sort()
					if each not in List:
						List.append(each)
			while k > 1 and nums[k] == nums[k-1]:
				k -= 1
			k -= 1
		return List
