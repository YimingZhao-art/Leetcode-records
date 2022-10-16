#include <iostream>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode() : val(0), next(nullptr) {}
	ListNode(int x) : val(x), next(nullptr) {}
	ListNode(int x, ListNode *next) : val(x), next(next) {}
	static ListNode * readInHead(int n) {
		ListNode * head = new ListNode(0);
		auto curr = head;
		int * a = new int[n];
		int i = 0;
		while ( cin >> a[i] ) i++;
		for ( i = 0; i <7; i++ ) {
			curr->next = new ListNode(*(a+i));
			curr = curr->next;
		}
		return head->next;
	}
	void printFromHere() {
		ListNode * x = this;
		while (x) {
			cout << x->val << " ";
			x = x->next;
		}
	}
};

class Solution {
public:
	ListNode * deleteDuplicates(ListNode * head) {
		ListNode * newHead = new ListNode(-101, head);
		ListNode * curr = newHead;
		while ( head ) {
			if ( head->next && head->val == head->next->val ) {
				while ( head->next && head->val == head->next->val ) {
					head->next = head->next->next;
				curr->next = head->next;
			
				}
			}
			else {
				curr = curr->next;
			}
			head = head->next;
		}
		return newHead->next;
	}
};


int main(int argc, char *argv[]) {
	
	
	Solution * s = new Solution();
	
	auto head = ListNode::readInHead(7);
	
	auto x = s->deleteDuplicates(head);
	
	(*x).printFromHere();
	
	
}