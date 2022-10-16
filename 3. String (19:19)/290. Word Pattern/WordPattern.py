#!/usr/bin/env python3
from typing import List

class Solution:
	def wordPattern(self, pattern: str, s: str) -> bool:
		s = s.split()
		p2s = {}
		s2p = {}
		if len(s) != len(pattern):
			return False
		for i in range(len(s)):
			if pattern[i] in p2s and p2s[pattern[i]] != s[i]:
				return False
			if s[i] in s2p and s2p[s[i]] != pattern[i]:
				return False
			p2s[pattern[i]] = s[i]
			s2p[s[i]] = pattern[i]
		return True

def main():
	
	
if __name__ == "__main__":
	main()