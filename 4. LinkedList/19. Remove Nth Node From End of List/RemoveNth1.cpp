#include <iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
};
class Solution {
public:
	
	int countTotal(ListNode* head) {
		int count = 0;
		while (head) {
			count++;
			head = head->next;
		}
		return count;
	}
	
	ListNode * removeNthFromEnd(ListNode * head, int n) {
		int total = countTotal(head);
		int i = 0;
		
		ListNode * pre, *newHead = new ListNode(0, head), *curr=newHead;
		while ( i != total - n + 1 ) {
			pre = curr;
			curr = curr->next;
			i++;
		}
		pre->next = curr->next;
		return newHead->next;
	}
};
int main(int argc, char *argv[]) {
	
}