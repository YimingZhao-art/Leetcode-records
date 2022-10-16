#!/usr/bin/env python3
from typing import List

class Solution:
	def myAtoi(self, s: str) -> int:
		if s == "":
			return 0
		
		i, l, tag, ans = 0, len(s), 1, ""
		
		while i < l:
			if s[i] == " ":
				if i > 1 and s[i-1] != " ":
					return 0
				i += 1
				continue
			
			if i < l-1 and s[i] in "+-" and s[i+1]  not in "0123456789":
				return 0
			if i < l-1 and s[i] not in "+-0123456789" and s[i+1] in "0123456789":
				return 0
			
			if s[i] in "0123456789" or s[i] in "+-":
				if s[i] in "+-":
					if i == l-1:
						return 0
					if s[i] == "-":
						tag = -1
					i += 1
				while i < l and s[i] in "0123456789":
					ans += s[i]
					i += 1
				if int(ans)*tag < -2**31:
					return -2**31
				elif int(ans)*tag > 2**31-1:
					return 2**31-1
				else:
					return int(ans)*tag
			i += 1
			
		return 0
	
			
			
		
		

def main():
	s = "0000-"
	sol = Solution()
	print(sol.myAtoi(s))
	
if __name__ == "__main__":
	main()