#!/usr/bin/env python3
from typing import List

class Solution:
	def licenseKeyFormatting(self, s: str, k: int) -> str:
		stack = []
		for each in s:
			if each == '-':
				continue
			if each.isalpha():
				stack.append(each.upper())
			else:
				stack.append(each)
		key = ""
		
		for i in range(len(stack)-1, -1, -1):
			
			key += stack[i]
			if i == 0:
				break
			if (len(stack)-1-i+1) % k == 0:
				key += '-'
			
		return "".join(reversed(key))
				
		

def main():
	print(Solution().licenseKeyFormatting("2-5g-3-J", 2))
	
if __name__ == "__main__":
	main()