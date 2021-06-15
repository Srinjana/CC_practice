#include<stdio.h>
#include<conio.h>
#include<stdlib.h>


struct node 
{
    int key;
    struct node *left, *right;
};


struct node *newNode (int item)
{
    struct node *temp = (struct node *) malloc(sizeof(struct node));
    // Node *temp = new Node;
    temp -> key = item;
    temp -> left = temp -> right = NULL;
    return temp;
   
};

void kth_largest (struct node *root, int k, int c)
{
	//	base case
	if (root == NULL || c >= k)
	return;
	
	//	largest element visited first
	kth_largest(root -> right, k, c);
	
	c++;
	
	if (c == k)  // its the kth largest
	{
		printf("\n K'th largest element is: %d \n",root->key);
		return;
	}
	
	// recursion for left subtree
	kth_largest(root -> left, k, c);
	
}

void find_max (struct node *root, int k)
{
	int c = 0;
	
	kth_largest(root, k, c);
}

struct node *insert_node (struct node *node, int key)
{
    // tree is empty
    if (node == NULL)
    return newNode(key);

    // recur down the tree
    if (key < node -> key)
    {
        node->left = insert_node(node->left, key);
    }
    else if (key > node -> key)
    {
        node->right = insert_node(node->right, key);
    }
    return node;

}

int main()
{
    /* Let us create following BST
              50
           /     \
          30      70
         /  \    /  \
       20   40  60   80 */

    struct node *root = NULL;
    int c = 0;
    root = insert_node(root, 50);
    insert_node(root, 30);
    insert_node(root, 20);
    insert_node(root, 40);
    insert_node(root, 70);
    insert_node(root, 60);
    insert_node(root, 80);
	
	int k;
    for (int k = 1; k <= 7; k++)
        {
        	find_max(root, k);
		}
    
    return 0;
}
