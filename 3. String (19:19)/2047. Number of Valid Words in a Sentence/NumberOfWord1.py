#!/usr/bin/env python3
from typing import List
import re

class Solution:
	def countValidWords(self, sentence: str) -> int:
		pattern = re.compile(r'(^[a-z]+(-[a-z]+)?)?[,.!]?$')
		return sum(bool(pattern.match(word)) for word in sentence.split())
	
def main():
	sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener."
	print(Solution().countValidWords(sentence))
	
if __name__ == "__main__":
	main()