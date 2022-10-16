#!/usr/bin/env python3
from typing import List

class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		i = len(s)-1
		count = 0
		while i > -1:
			if s[i] == " ":
				i -= 1
				continue
			while i > -1 and s[i] != " ":
				count += 1
				i -= 1
			if i > -1 and s[i] == " ":
				return count
		return count

def main():
	s = "   fly me   to   the moon  "
	print(Solution().lengthOfLastWord(s))
	
	
if __name__ == "__main__":
	main()