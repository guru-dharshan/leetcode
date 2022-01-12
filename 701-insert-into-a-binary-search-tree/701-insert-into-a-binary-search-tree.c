/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


struct TreeNode* insertIntoBST(struct TreeNode* root, int data){
    if(root==NULL){
        root= (struct TreeNode*)malloc(sizeof(struct TreeNode));
        root->val=data;
        root->right=NULL;
        root->left=NULL;
       
    }
    else if(data<=root->val){
        root->left=insertIntoBST(root->left,data);
    }
    else{
        root->right=insertIntoBST(root->right,data);
    }
    return root;

}