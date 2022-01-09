/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* head=(struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* temp=head;
    
    int c=0;
    int f=0;
    int a,b;
    while(l1!=NULL || l2!=NULL){
        if(l1!=NULL){
            a=l1->val;
        }
        if(l2!=NULL){
            b=l2->val;
        } 
        f=a+b+c;
        c=0;
        if(f>=10){
        c=f/10;
        f=f%10;
        }
        
        //creating node
        struct ListNode* tempdata=(struct ListNode*)malloc(sizeof(struct ListNode));
        tempdata->val=f;
        tempdata->next=NULL;
        //inserting node to ans
        if(head==NULL){
            head=tempdata;
            temp=head;
        }
        else{
            temp->next=tempdata;
            temp=tempdata;
        }
        a=0;b=0;
        if(l1!=NULL){
                   l1=l1->next;
 
        }
        if(l2!=NULL){
                    l2=l2->next;

        }
        
        
     }
    if(c>0){
          struct ListNode* tempdata=(struct ListNode*)malloc(sizeof(struct ListNode));
        tempdata->val=c;
        tempdata->next=NULL;
        temp->next=tempdata;
    }
    
    return head->next;

}