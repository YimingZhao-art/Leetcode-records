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
	ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
		if ( list1 == NULL ) return list2;
		else if ( list2 == NULL ) return list1;
		ListNode * dummy = new ListNode(0), *curr = dummy;
		while ( list1 && list2 ) {
			if ( list1->val < list2->val ) {
				curr->next = new ListNode(list1->val);
				list1 = list1->next;
				curr = curr->next;
			}
			else {
				curr->next = new ListNode(list2->val);
				list2 = list2->next;
				curr = curr->next;
			}
		}
		while (list1)  {
			curr->next = new ListNode(list1->val);
			list1 = list1->next;
			curr = curr->next;
		}
		while (list2)  {
			curr->next = new ListNode(list2->val);
			list2 = list2->next;
			curr = curr->next;
		}
		return dummy->next;
	}
};

int main(int argc, char *argv[]) {
	
}