#!/usr/bin/env python3
from typing import List
from collections import Counter

class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		s, g = Counter(secret), Counter(guess)
		a = sum(i == j for i, j in zip(secret, guess))
		return '%sA%sB' % (a, sum((s & g).values()) - a)
	

def main():
	secret = "1123"
	guess = "0111"
	print(Solution().getHint(secret, guess))
	
if __name__ == "__main__":
	main()