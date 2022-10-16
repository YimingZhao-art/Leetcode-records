#!/usr/bin/env python3
from typing import List

class Solution:
	def candyCrush(self, board: List[List[int]]) -> None:
		m = len(board)
		n = len(board[0])
		
		while True:
			myDict = {}
			sinkDict = {}
			
			def countSame(i,j):
				k = board[i][j]
				xListCol = [i-1, i+1]
				yListCol = [j, j]
				xListRow = [i, i]
				yListRow = [j-1, j+1]
				
				#judge horizontally
				if j > 0 and j < n-1:
					if k == board[i][j-1] and board[i][j+1] == k:
						myDict[(i,j)] = True
						leftJ, rightJ = j-1, j+1
						while leftJ > -1 and board[i][leftJ] == k:
							myDict[(i,leftJ)] = True
							leftJ -= 1
						while rightJ < n and board[i][rightJ] == k:
							myDict[(i,rightJ)] = True
							rightJ += 1
				#judge vertically
				if i > 0 and i < m-1:
					if k == board[i-1][j] and k == board[i+1][j]:
						myDict[(i,j)] = True
						upI, downI = i-1, i+1
						while upI > -1 and board[upI][j] == k:
							myDict[(upI,j)] = True
							upI -= 1
						while downI < m and board[downI][j] == k:
							myDict[(downI,j)] = True
							downI += 1
							
			for i in range(m):
				for j in range(n):
					if board[i][j] != 0:
						count = countSame(i, j)
			for (i,j) in myDict:
				board[i][j] = 0
				if j not in sinkDict:
					sinkDict[j] = [i]
				else:
					sinkDict[j].append(i)
#			printBoard(board)
#			print("~~~~~~~~~~~~~~~~~~~~~~~~")
			
			for j in sinkDict:
				L = []
				for i in range(m-1,-1,-1):
					if board[i][j] != 0:
						L.append(board[i][j])
				
				for i in range(len(L)):
					board[m-1-i][j] = L[i]
				for i in range(m-len(L)):
					board[i][j] = 0
#			printBoard(board)
#			print("------------------------")
			
			if myDict == {}:
#				print(id(board))
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