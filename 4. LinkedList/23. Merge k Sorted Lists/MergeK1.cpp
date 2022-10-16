#include <iostream>
#include <vector>
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
		for ( i = 0; i <n; i++ ) {
			cin >> a[i];
		}
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
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		if ( lists.size() == 0 ) return NULL;
		int idMin;
		ListNode * dummy = new ListNode(0), *minCurr = NULL, *dummyCurr = dummy;
		for (int i = 0; i < lists.size(); i++ ) {
			if ( lists[i] ) {
				minCurr = lists[i];
				idMin = i;
				break;
			}
		}
		if ( !minCurr ) return NULL;
		while ( minCurr ) {
			for (int i = 0; i < lists.size(); i++ ) {
				if ( lists[i] && lists[i]->val < minCurr->val ) {
					minCurr = lists[i];
					idMin = i;
				}
			}
			dummyCurr->next = new ListNode(minCurr->val);
			dummyCurr = dummyCurr->next;
			lists[idMin] = lists[idMin]->next;
			bool t = false;
			for (int i = 0; i < lists.size(); i++ ) {
				if ( lists[i] ) {
					minCurr = lists[i];
					idMin = i;
					t = true;
					break;
				}
			}
			if (!t) return dummy->next;
		}
		return dummy->next;
	}
};

int main(int argc, char *argv[]) {
	
}