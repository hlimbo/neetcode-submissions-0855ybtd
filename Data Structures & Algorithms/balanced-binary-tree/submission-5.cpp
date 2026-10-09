/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

 /*

    Base case: null root tree will always return true

    Recursive Step: 
        * calculate height of tree
            1 + max(recur(root.left), recur(root.right))
    
    Formula: abs diff (height of left subtree - height of right subtree) < 2 then the subtree is balanced otherwise return false if one of the subtrees is not balanced
    ^ This has to be true for ALL SUBTREES so I need to use the && operator
 */

class Solution {
public:
    // counts number of edges of the binary tree
    int getHeight(TreeNode* root) {
        if (root == nullptr) {
            return -1;
        }

        return 1 + std::max(getHeight(root->left), getHeight(root->right));
    }

    int isBalancedHelper(TreeNode* root, bool* isBalanced) {
        if (root == nullptr) {
            return -1;
        }

        int leftHeight = isBalancedHelper(root->left, isBalanced);
        int rightHeight = isBalancedHelper(root->right, isBalanced);

        int heightDiff = abs(leftHeight - rightHeight);\
        int height = 1 + max(leftHeight, rightHeight);
        if (heightDiff > 1) {
            *isBalanced = false;
        }

        return height;
    }

    bool isBalanced(TreeNode* root) {
        if (root == nullptr) {
            return true;
        }

        bool areAllTreesBalanced = true;
        int treeHeight = isBalancedHelper(root, &areAllTreesBalanced);

        return areAllTreesBalanced;

        // int leftHeight = getHeight(root->left);
        // int rightHeight = getHeight(root->right);
        // bool isCurrTreeBalanced = abs(leftHeight - rightHeight) < 2;

        // return isCurrTreeBalanced && isBalanced(root->left) && isBalanced(root->right);
    }
};
