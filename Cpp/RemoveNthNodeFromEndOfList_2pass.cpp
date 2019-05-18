/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    int getSize(ListNode* head){
        ListNode* p=head;
        int L=0;
        while(p){
            L++;
            p=p->next;
        }
        return L;
    }
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int size=getSize(head);
        if(size==n)   //specific condition, the first position have not privious
            return head->next;
        ListNode* p=head;
        for(int i=0;i<size-n-1;i++){  //move to the position before deleted position
            p=p->next;
        }
        p->next=p->next->next;
        return head;
    }
};