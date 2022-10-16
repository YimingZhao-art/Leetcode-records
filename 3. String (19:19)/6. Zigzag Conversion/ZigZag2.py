#!/usr/bin/env python3
from typing import List

class Solution:
	def convert(self, s: str, numRows: int) -> str:
		l = len(s)
		times = 2*numRows - 2
		if times == 0:
			return s
		
		ans = ""
		
		
		for row in range(numRows):
			for i in range(row, l, times):
				if row == 0 or row == numRows-1:
					ans += s[i]
				else:
					j = ((i//times)*2+1)*times-i
					if j < l:
						#ansL[row] += s[i] + (times-2-row)*" " + s[j] + (row-1)*" "
						ans += s[i] + s[j]
					else:
						#ansL[row] += s[i] + (times-2-row)*" "
						ans += s[i]
		
				
		return ans
		
def main():
	s = "PAYPALISHIRING"
	numRows = 3
	print(Solution().convert(s, numRows))
	
if __name__ == "__main__":
	main()