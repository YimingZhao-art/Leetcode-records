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
	ListNode * deleteDuplicates(ListNode * head) {
		ListNode *dummy=new ListNode(0,head);
		ListNode *prev=dummy;
		
		while(head!=NULL){
			
			if(head->next!=NULL && head->val==head->next->val){
				
				while(head->next!=NULL && head->val==head->next->val) {
					head=head->next;
				}
				cout << head->val << " ";
				
				prev->next=head->next;
			}
			
			else prev=prev->next;
			
			
			head=head->next;
		}
		
		return dummy->next;
	}
};


int main(int argc, char *argv[]) {
	ListNode * head = new ListNode(0);
	auto curr = head;
	int a[7] = {1,2,3,3,4,4,5};
	for ( int i:a ) {
		curr->next = new ListNode(i);
		curr = curr->next;
	}
	Solution * s = new Solution();
	head = head->next;
	auto x = s->deleteDuplicates(head);
	while (x) {
		cout << x->val << " ";
		x = x->next;
	}
}