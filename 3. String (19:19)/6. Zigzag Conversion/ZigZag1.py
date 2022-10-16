#!/usr/bin/env python3
from typing import List

class Solution:
	def convert(self, s: str, numRows: int) -> str:
		l = len(s)
		times = 2*numRows - 2
		if times == 0:
			return s
		ansL = []
		for i in range(numRows):
			_ = ""
			ansL.append(_)
		
		for row in range(numRows):
			if row == 0 or row == numRows-1:
				for i in range(row, l, times):
					#ansL[row] += s[i] + " "*(numRows-2)
					ansL[row] += s[i]
			else:
				for i in range(row, l, times):
					j = ((i//times)*2+1)*times-i
					if j < l:
						#ansL[row] += s[i] + (times-2-row)*" " + s[j] + (row-1)*" "
						ansL[row] += s[i] + s[j]
					else:
						#ansL[row] += s[i] + (times-2-row)*" "
						ansL[row] += s[i]
		
		ans = ""
		for each in ansL:
			ans += each
		ans.strip()
		return ans
		
def main():
	s = "PAYPALISHIRING"
	numRows = 3
	print(Solution().convert(s, numRows))
	
if __name__ == "__main__":
	main()