#!/usr/bin/env python3
from typing import List

class Solution:
	def valid(self, nums: List[str]) -> bool:
		myDict = {}
		for i in range(1,10):
			myDict[str(i)] = False
		for num in nums:
			if num == ".":
				continue
			else:
				if myDict[num] == True:
					return False
				else:
					myDict[num] = True
		return True
	
	def isValidSudoku(self, board: List[List[str]]) -> bool:
		ans = True
		for i in range(9):
			if self.valid(board[i]) == False:
				return False
			
		for j in range(9):
			L = []
			for i in range(9):
				L.append(board[i][j])
			if not self.valid(L):
				return False
		
		for i in range(0,9,3):
			for j in range(0,9,3):
				L = []
				L.append(board[i][j])
				L.append(board[i+1][j])
				L.append(board[i+2][j])
				L.append(board[i][j+1])
				L.append(board[i][j+2])
				L.append(board[i+1][j+1])
				L.append(board[i+1][j+2])
				L.append(board[i+2][j+1])
				L.append(board[i+2][j+2])
				if not self.valid(L):
					return False
		
		return ans
		

def main():
	board=[
		["9",".",".","6",".",".",".",".","."],
		[".",".",".",".","6",".",".",".","."],
		[".",".",".",".",".","1",".","3","."],
		[".",".",".",".",".",".",".",".","8"],
		[".",".",".",".",".","8",".",".","."],
		[".",".",".","4",".",".","2",".","."],
		[".",".",".",".",".",".",".",".","1"],
		["6",".",".",".","1",".",".",".","."],
		[".",".",".",".",".",".",".",".","."]]
	i=0
	j=3
	L = []
	L.append(board[i][j])
	L.append(board[i+1][j])
	L.append(board[i+2][j])
	L.append(board[i][j+1])
	L.append(board[i][j+2])
	L.append(board[i+1][j+2])
	L.append(board[i+2][j+1])
	L.append(board[i+2][j+2])
	print(L)
	
	sol = Solution()
	print(sol.isValidSudoku(board))
	
if __name__ == "__main__":
	main()