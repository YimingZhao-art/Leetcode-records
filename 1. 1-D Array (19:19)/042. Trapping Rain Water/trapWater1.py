#!/usr/bin/env python3

'''
[10527,740,9013,1300,29680,4898,139...
'''


from typing import List

class Solution:
	def trap(self, height: List[int]) -> int:
		L = len(height)
		l, r = 0, L-1
		leftMax, rightMax, ans = 0, 0, 0
		
		while l < r:
			if height[l] < height[r]:
				leftMax = max(leftMax, height[l])
				ans += leftMax-height[l]
				l += 1
			else:
				rightMax = max(rightMax, height[r])
				ans += rightMax-height[r]
				r -=1
		return ans

def main():
	sol = Solution()
	num = input().split(',')
	for i in range(len(num)):
		num[i] = int(num[i].strip())
		
	print(sol.trap(num))
	
	
if __name__ == "__main__":
	main()