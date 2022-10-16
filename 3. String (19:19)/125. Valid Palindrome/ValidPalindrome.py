#!/usr/bin/env python3
from typing import List

class Solution:
	def isPalindrome(self, s: str) -> bool:
		if len(s) == 0:
			return False
		left,right = 0, len(s)-1
		while left < right:
			while left < right and not s[left].isalnum():
				left += 1
			while left < right and not s[right].isalnum():
				right -= 1
			if s[left].lower() != s[right].lower():
				return False
			while left < right and s[left].lower() == s[right].lower():
				left += 1
				right -= 1
		return True
				

def main():
	sol = Solution()
	s = "0p"
	print(sol.isPalindrome(s))
	
if __name__ == "__main__":
	main()