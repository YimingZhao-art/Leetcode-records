#!/usr/bin/env python3
from typing import List
class Solution:
		
	def gameOfLife(self, board: List[List[int]]) -> None:
		m = len(board)
		n = len(board[0])
		
		
		
		for i in range(m):
			for j in range(n):
				count = 0
				
				indexListX = [i-1, i-1, i-1, i, i, i+1, i+1, i+1]
				
				indexListY = [j-1, j, j+1, j-1, j+1, j-1, j, j+1]
				
				for _ in range(8):
					if indexListX[_] >= 0 and indexListX[_] < m and indexListY[_] >= 0 and indexListY[_] < n:
						if board[indexListX[_]][indexListY[_]]%10 == 1:
							count += 1
				if board[i][j] == 0:
					if count == 3:
						board[i][j] += 10
				else:
					if count < 2 or count > 3:
						board[i][j] += 10
						
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