#!/usr/bin/env python3
from typing import List
class Solution:
	def countLayer1(self, height: List[int], unitDepth: int) -> int:
		count = 0
		if len(height) < 2:
			return 0
		i, j = 0, 0
		while i < len(height) and height[i] < 1:
			i += 1
		j += 1
		while j < len(height):
			while i < len(height)-1 and height[i+1] > 0:
				i += 1
			j = i + 1
			
			while j < len(height) and height[j] < 1:
				j += 1
			if j >= len(height) or height[j] < 1:
				return count
			else:
				count += (j-i-1)*unitDepth
				i = j
				j = i + 1
			
				
		return count
	
	def deriveStep(self, height: List[int]) -> int:
		minPositive = 0
		for i in height:
			if i > 0:
				if minPositive == 0:
					minPositive = i
				elif i < minPositive:
					minPositive = i
		return minPositive
	
	def trap(self, height: List[int]) -> int:
		count = 0
		unitDepth = self.deriveStep(height)
		while  unitDepth > 0:
			count += self.countLayer1(height, unitDepth)
#			print(count)
			for i in range(len(height)):
				height[i] -= unitDepth
			unitDepth = self.deriveStep(height)
		return count
	
	

def main():
	sol = Solution()
	num = input().split(',')
	for i in range(len(num)):
		num[i] = int(num[i].strip())
	
	print(sol.trap(num))
	
if __name__ == "__main__":
	main()