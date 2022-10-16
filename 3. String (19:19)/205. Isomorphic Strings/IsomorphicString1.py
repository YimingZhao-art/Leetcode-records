#!/usr/bin/env python3
from typing import List

class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		s2t = {}
		t2s = {}
		
		for i in range(len(s)):
			if s[i] in s2t and t[i] != s2t[s[i]]:
				return False
			if t[i] in t2s and s[i] != t2s[t[i]]:
				return False
			s2t[s[i]] = t[i]
			t2s[t[i]] = s[i]
		return True
	
def main():
	s = "paper"
	t = "title"
	
	print(Solution().isIsomorphic(s, t))
	
if __name__ == "__main__":
	main()