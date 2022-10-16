#!/usr/bin/env python3
from typing import List

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		s = s.split()
		for each in s:
			each.strip()
		return len(s[-1])
	
def main():
	s = "   fly me   to   the moon  "
	print(Solution().lengthOfLastWord(s))
	
if __name__ == "__main__":
	main()