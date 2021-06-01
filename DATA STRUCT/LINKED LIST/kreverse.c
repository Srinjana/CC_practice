// Given a linked list of size N.The task is to reverse every k nodes(where k is an input to the function) in the linked list.
#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

struct Node* Reverse (struct Node* head, int k)
{
    struct Node *start = head;
    struct Node *r = NULL;
    struct Node *s;
    int count = 0;

    while (start != NULL && count < k)
    {
        s = r;
        r = start;
        start = start->next;
        r->next = s;
        count++;
    }

    if (start != NULL)
        head->next = Reverse(start, k);

    return r;
}

void push(struct Node **head_ref, int new_data)
{
    /* allocate node */
    struct Node *new_node =
        (struct Node *)malloc(sizeof(struct Node));

    /* put in the data  */
    new_node->data = new_data;

    /* link the old list off the new node */
    new_node->next = (*head_ref);

    /* move the head to point to the new node */
    (*head_ref) = new_node;
}

/* Function to print linked list */
void printList(struct Node *node)
{
    while (node != NULL)
    {
        printf("%d  ", node->data);
        node = node->next;
    }
}

/* Driver program to test above function*/
int main(void)
{
    /* Start with the empty list */
    struct Node *head = NULL;

    /* Created Linked list is 1->2->3->4->5->6->7->8->9 */
    push(&head, 9);
    push(&head, 8);
    push(&head, 7);
    push(&head, 6);
    push(&head, 5);
    push(&head, 4);
    push(&head, 3);
    push(&head, 2);
    push(&head, 1);

    printf("\nGiven linked list \n");
    printList(head);
    head = Reverse(head, 3);

    printf("\nReversed Linked list \n");
    printList(head);

    return 0;
}
