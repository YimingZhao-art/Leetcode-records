#!/usr/bin/env python3
from typing import List

class Solution:
	def countBattleships(self, board: List[List[str]]) -> int:
		m = len(board)
		n = len(board[0])
		count = 0
		for i in range(m):
			for j in range(n):
				if board[i][j] != 'X':
					continue
				count += 1
				xList = [i-1, i]
				yList = [j, j-1]
				repeat = False
				for _ in range(2):
					if xList[_] > -1 and xList[_] < m and yList[_] > -1 and yList[_] < n:
						if board[xList[_]][yList[_]] == "X":
							repeat = True
							break
				
				if repeat:
					count -= 1
		return count
				
						

def main():
	sol = Solution()
	print(sol.countBattleships([["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]))
	
if __name__ == "__main__":
	main()