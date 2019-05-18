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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* ans=new ListNode(0);
        ListNode* p1=l1;
        ListNode* p2=l2;
        ListNode* p3=ans;
        int carry=0;
        while(p1 || p2){
            int x=p1?p1->val:0;
            int y=p2?p2->val:0;
            int sum=x+y+carry;
            p3->next=new ListNode(sum%10);
            carry=sum/10;
            if(p1)
                p1=p1->next;
            if(p2)
                p2=p2->next;
            p3=p3->next;
        }
        if(carry)
            p3->next=new ListNode(carry);
        
           return ans->next;
    }
};