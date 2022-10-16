#!/usr/bin/env python3
from typing import List

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		count = 0
		for _ in ransomNote:
			if _ in magazine:
				k = magazine.find(_)
				magazine = magazine[:k] + "_" +magazine[k+1:] if k+1 < len(magazine) else magazine[:k] + "_"
				count += 1
	
		return count == len(ransomNote)
	
def main():
	sol = Solution()
	ranS = "aa"
	magS = "aab"
	print(sol.canConstruct(ranS, magS))
	
if __name__ == "__main__":
	main()