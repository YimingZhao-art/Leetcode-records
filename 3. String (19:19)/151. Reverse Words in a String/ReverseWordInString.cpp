#include <iostream>

using namespace std;

class Solution {
public:
	void reverseWord(string & s, int i, int j) {
		while (i < j) {
			char temp = s[i];
			s[i++] = s[j];
			s[j--] = temp;
		}
	}
	
	string reverseWords(string & s) {
		int len = s.length();
		int i = 0, j = 0, l = 0;
		int wordcount = 0;
		
		while (true) {
			while (i<len && s[i] == ' ') i++;
			if (i==len) break;
			if (wordcount) s[j++] =' ';
			l = j;
			while (i<len && s[i] != ' ') {
				s[j]=s[i];
				j++;
				i++;
			}
			reverseWord(s, l, j-1);
			wordcount++;
		}
		s.resize(j);
		reverseWord(s, 0, j-1);
		return s;
	}
};

int main(int argc, char *argv[]) {
	
}