#!/usr/bin/env python3
from typing import List

class Solution:
	def canConstruct(self, ransomNote: str, magazine: str) -> bool:
		if ransomNote == "":
			return True
		s = sorted(list(ransomNote))
		t = sorted(list(magazine))
		ans = False
		i = 0
		s_len = len(s)
		
		
		t_len = len(t)
		
		for j in range(t_len):
			if t[j] == s[i]:
				i += 1
			if i == s_len:
				return True
			
		return ans

def main():
	sol = Solution()
	ranS = "aa"
	magS = "aab"
	print(sol.canConstruct(ranS, magS))
	
if __name__ == "__main__":
	main()