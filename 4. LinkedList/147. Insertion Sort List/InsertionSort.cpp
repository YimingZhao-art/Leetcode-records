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
	ListNode* insertionSortList(ListNode* head) {
		ListNode * ansHead = new ListNode(0,new ListNode(head->val)),*prev, *curr;
		head = head->next;
		
		while (head) {
			
			prev = ansHead;
			curr = ansHead->next;
			
			while ( curr && head->val > curr->val ) {
				prev = curr;
				curr = curr->next;
			}

			prev->next = new ListNode(head->val,curr);
			head = head->next;
		}
		return ansHead->next;
	}
};

int main(int argc, char *argv[]) {
	ListNode * head = new ListNode(0);
	auto curr = head;
	int a[4] = {4,2,1,3};
	for ( int i:a ) {
		curr->next = new ListNode(i);
		curr = curr->next;
	}
	Solution * s = new Solution();
	head = head->next;
	auto x = s->insertionSortList(head);
	while (x) {
		cout << x->val << " ";
		x = x->next;
	}
}