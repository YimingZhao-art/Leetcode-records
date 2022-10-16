#!/usr/bin/env python3
from typing import List

class Solution:
	def removePalindromeSub(self, s):
		if s == "":
			return 0
		elif s[::-1] == s:
			return 1
		else:
			return 2

def main():
	s = "abbabbba"
	print(Solution().removePalindromeSub(s))
	
if __name__ == "__main__":
	main()