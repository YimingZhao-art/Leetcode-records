#!/usr/bin/env python3
from typing import List

class Solution:
	def isSubsequence(self, s: str, t: str) -> bool:
		ans = False
		i = 0
		s_len = len(s)
		if s_len == 0:
			return True
		t_len = len(t)
	
		for j in range(t_len):
			if t[j] == s[i]:
				i += 1
			if i == s_len:
				return True
			
		return ans

def main():
	
	
if __name__ == "__main__":
	main()