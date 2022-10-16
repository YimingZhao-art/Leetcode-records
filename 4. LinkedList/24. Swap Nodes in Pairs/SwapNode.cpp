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
		for ( i = 0; i <n; i++ ) {
			curr->next = new ListNode(*(a+i));
			curr = curr->next;
		}
		delete [] a;
		return head->next;
	}
	void printFromHere() {
		ListNode * x = this;
		while (x) {
			cout << x->val << " ";
			x = x->next;
		}
		cout << endl;
	}
};

class Solution {
public:
	ListNode* swapPairs(ListNode* head) {
		if ( !head || !head->next ) return head;
		ListNode * dummy = new ListNode(0, head), *prev = dummy, *next = head->next;
		while ( head && next ) {
			prev->next = next;
			head->next = next->next;
			next->next = head;
			
			prev = head;
			head = prev->next;
			if (!head) return dummy->next;
			else next = head->next;
		}
		
		return dummy->next;
	}
};

int main(int argc, char *argv[]) {
	
}