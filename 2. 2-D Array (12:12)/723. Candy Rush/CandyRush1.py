#!/usr/bin/env python3
from typing import List

class Solution:
	def candyCrush(self, board: List[List[int]]) -> None:
		m = len(board)
		n = len(board[0])
		crush = False
		for i in range(m):
			for j in range(n):
				if board[i][j] == 0:
					continue
				v = abs(board[i][j])
				
				if i < m-2 and abs(board[i+1][j]) == v and abs(board[i+2][j]) == v:
					board[i][j] = board[i+1][j] = board[i+2][j] = -v
					crush = True
				
				if j < n-2 and abs(board[i][j+1]) == v and abs(board[i][j+2]) == v:
					board[i][j] = board[i][j+1] = board[i][j+2] = -v
					crush = True
		
		for j in range(n):
			i = m-1
			for p in range(m-1,-1,-1):
				if board[p][j] > 0:
					board[i][j] = board[p][j]
					i -= 1
			while i > -1:
				board[i][j] = 0
				i -= 1
		
		if crush:
			self.candyCrush(board)
		else:
			return

def printBoard(board):
	m = len(board)
	n = len(board[0])
	for i in range(m):
		for j in range(n):
			print(f"{board[i][j]:4}", end=" ")
		print()
		
def main():
	board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
	sol = Solution()
	#printBoard(board)
	sol.candyCrush(board)
	print("------------------------")
	printBoard(board)
	print(board == [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]])
	
	
	
	
	
if __name__ == "__main__":
	main()