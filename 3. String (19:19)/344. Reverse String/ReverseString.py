#!/usr/bin/env python3
from typing import List

class Solution:
	def reverseString(self, s: List[str]) -> None:
		for i in range(int(len(s)/2)):
			s[i], s[-1-i] = s[-1-i],s[i]
			

def main():
	
	
if __name__ == "__main__":
	main()