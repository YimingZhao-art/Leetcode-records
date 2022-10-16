#!/usr/bin/env python3
from typing import List

class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		ans = ''
		count = 0
		s = s.replace('-', '').upper()[::-1]
		for i in range(len(s)):
			ans += s[i]
			if i == len(s)-1:
				break
			if (i+1)%k == 0:
				ans += '-'
		return ans[::-1]
	
		

def main():
	print(Solution().licenseKeyFormatting("2-5g-3-J", 2))
	
if __name__ == "__main__":
	main()