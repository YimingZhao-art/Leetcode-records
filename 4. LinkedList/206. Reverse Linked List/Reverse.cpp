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
	ListNode * reverseList(ListNode* head) {
		if (!head) return NULL;
		ListNode * dummy = new ListNode(0, new ListNode(head->val));
		head = head->next;
		while ( head ) {
			auto next = dummy->next;
			dummy->next = new ListNode(head->val, next);
			head = head->next;
		}
		return dummy->next;
	}
};

int main(int argc, char *argv[]) {
	auto head = ListNode::readInHead(5);
	auto x = (new Solution())->reverseList(head);
	x->printFromHere();
	
}