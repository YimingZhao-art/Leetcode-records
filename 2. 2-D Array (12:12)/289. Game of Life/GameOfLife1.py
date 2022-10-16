#!/usr/bin/env python3
from typing import List
from copy import deepcopy
class Solution:
	def countAliveNeighbours(self,board,i,j):
		indexListX = [i-1, i-1, i-1, i, i, i+1, i+1, i+1]
		indexListY = [j-1, j, j+1, j-1, j+1, j-1, j, j+1]
		count = 0
		for _ in range(8):
			if board[indexListX[_]][indexListY[_]]%10 == 1:
				count += 1
		return count
	
	
	def gameOfLife(self, board: List[List[int]]) -> None:
		m = len(board)
		n = len(board[0])
		
		_ = []
		for i in range(n+2):
			_.append(0)
		board.insert(0, _)
		__ = _[:]
		board.append(__)
		for i in range(1,m+1):
			board[i].insert(0, 0)
			board[i].append(0)
		
		for i in range(1, m+1):
			for j in range(1, n+1):
				count = self.countAliveNeighbours(board, i, j)
				if board[i][j] == 0:
					if count == 3:
						board[i][j] += 10
				else:
					if count < 2 or count > 3:
						board[i][j] += 10
		board.pop(m+1)
		board.pop(0)
		for i in range(m):
			board[i].pop(n+1)
			board[i].pop(0)
		
		for i in range(m):
			for j in range(n):
				if board[i][j] == 10:
					board[i][j] = 1
				elif board[i][j] == 11:
					board[i][j] = 0
		

def main():
	board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
	print(board)
	sol = Solution()
	sol.gameOfLife(board)
	print(board)
	
if __name__ == "__main__":
	main()