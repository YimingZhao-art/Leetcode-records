#!/usr/bin/env python3
from typing import List

class Solution:
	def convert(self, s: str, numRows: int) -> str:
		if numRows == 1:
			return s
		rowArray = [""] *numRows
		rowId = 1
		down = True
		for char in s:
			rowArray[rowId-1] += char
			if rowId == 1:
				down = True
			elif rowId == numRows:
				down = False
			if down:
				rowId += 1
			else:
				rowId -= 1
				
		return "".join(rowArray)
		
def main():
	s = "PAYPALISHIRING"
	numRows = 3
	print(Solution().convert(s, numRows))
	
if __name__ == "__main__":
	main()