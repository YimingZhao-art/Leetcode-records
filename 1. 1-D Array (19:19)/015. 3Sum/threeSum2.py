from typing import List

class Solution:
	"""
	O(n^2)
	"""
	def twoSum(self, nums: List[int], target: int, left: int, right: int):
		List = []
		while left < right:
			# print(nums[left], nums[right], target)
			sumOfTwo = nums[left] + nums[right]
			if sumOfTwo == target:
				List.append([nums[left], nums[right], -target])
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
	
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		nums.sort()
		# print(nums)
		k = len(nums)-1
		List = []
		for i in range(k-1):
			# print(target)
			if i > 0 and nums[i] == nums[i-1]:
				continue
			L = self.twoSum(nums, -nums[i], i+1, k)
			if  L != []:
				for each in L:
					each.sort()
					List.append(each)
		return List
	