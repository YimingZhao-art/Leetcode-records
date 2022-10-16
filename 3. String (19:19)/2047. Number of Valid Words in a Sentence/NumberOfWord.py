#!/usr/bin/env python3
from typing import List
import re

class Solution:
	def countValidWords(self, sentence: str) -> int:
		L = sentence.split()
		count = 0
		for each in L:
			if re.findall(r"\d", each) != []:
				continue
			l = len(each)
			if each.count('-') > 1:
				continue
			a=each.find('-')
			if a == 0 or a == l-1:
				continue
			if a == -1 or (each[a-1]+each[a+1]).isalpha():
				if len(re.findall(r'!|,|\.', each)) == 0:
					print(each)
					count += 1
				elif len(re.findall(r'!|,|\.', each)) <= 1:
					if not each[-1].isalpha():
						print(each)
						count += 1
		
		
		return count
					
				
		

def main():
	sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
	print(Solution().countValidWords(sentence))
	
if __name__ == "__main__":
	main()