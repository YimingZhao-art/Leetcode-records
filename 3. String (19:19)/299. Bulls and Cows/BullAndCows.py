#!/usr/bin/env python3
from typing import List
from collections import Counter

class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		myDict = {}
		bulls, cows = 0, 0
		
		for i in range(len(secret)):
			if secret[i] == guess[i]:
				bulls += 1
				continue
			if secret[i] not in myDict:
				myDict[secret[i]] = 1
			else:
				myDict[secret[i]] += 1
		for i in range(len(secret)):
			if guess[i] != secret[i]:
				if guess[i] in myDict and myDict[guess[i]] > 0:
					cows += 1
					myDict[guess[i]] -= 1
		
		return f"{bulls}A{cows}B"

def main():
	secret = "1123"
	guess = "0111"
	print(Solution().getHint(secret, guess))
	
if __name__ == "__main__":
	main()