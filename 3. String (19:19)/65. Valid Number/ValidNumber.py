#!/usr/bin/env python3
from typing import List

import re

class Solution:
	def isNumber(self, s: str) -> bool:
		pattern1 = r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))[Ee][+-]?\d+$" if ('e' in s or 'E' in s) else r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))$"
		return bool(re.match(pattern1, s))

def main():
	s = ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93""-123.456e789","0e"]
	for each in s:
		print(each,":",Solution().isNumber(each))
	
if __name__ == "__main__":
	main()