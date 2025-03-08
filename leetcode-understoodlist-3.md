**Apna college(Deletion in Bst)**
```java
    TreeNode delNode(TreeNode root, int x) {
      
        // Base case
        if (root == null) {
            return root;
        }

        // If key to be searched is in a subtree
        if (root.key > x) {
            root.left = delNode(root.left, x);
        } else if (root.key < x) {
            root.right = delNode(root.right, x);
        } else {
            // If root matches with the given key

            // Case when root has 0 children
              if (root.left == null&&root.right == null) {
                return root.right;
            }
            
            // When root has only right child
            if (root.left == null) {
                return root.right;
            }

            // When root has only left child
            if (root.right == null) {
                return root.left;
            }

            // When both children are present
            TreeNode succ = getSuccessor(root);
            root.key = succ.key;
            root.right = delNode(root.right, succ.key);
        }
        return root;
    }
 
    // Note that it is not a generic inorder successor 
    // function. It mainly works when the right child
    // is not empty, which is the case we need in BST
    // delete. 
    TreeNode getSuccessor(Node curr) {
        curr = curr.right;
        while (curr != null && curr.left != null) {
            curr = curr.left;
        }
        return curr;
    }  


```
