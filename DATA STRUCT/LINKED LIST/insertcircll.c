/*
    Circular Singly Linked List implementation by C programming Language
    Operations: create list, insert item to tail, insert item to first, insert item to middle (any position),
        delete any item according to position, print full list

*/

#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
}*head;

void createList(int n);
void displayList();
void insertAtBeginning(int data);
void insertAtN(int data, int position);


int main()
{
    int n, data, choice = 1;

    head = NULL;

    while(choice != 0)
    {
        printf("=============================================");
        printf("\nCIRCULAR LINKED LIST FUNCTIONS");
        printf("\n 1. Create List\n");
        printf("2. Display list\n");
        printf("3. Insert at beginning\n");
        printf("4. Insert at any position\n");
        printf("0. Exit\n");
        printf("--------------------------------------------\n");
        printf("Enter your choice : ");

        scanf("%d", &choice);

        switch(choice)
        {
            case 1:
                printf("Enter the total number of nodes in list: ");
                scanf("%d", &n);
                createList(n);
                break;
            case 2:
                displayList(&head);
                break;
            case 3:
                printf("Enter data to be inserted at beginning: ");
                scanf("%d", &data);
                insertAtBeginning(data);
                break;
            case 4:
                printf("Enter node position: ");
                scanf("%d", &n);
                printf("Enter data you want to insert at %d position: ", n);
                scanf("%d", &data);
                insertAtN(data, n);
                break;
            case 0:
                break;
            default:
                printf("Error! Invalid choice. Please choose again");
        }

      printf("\n\n\n\n\n");
    }

    return 0;
}

void createList(int n)
{
    int i, data;
    struct Node *prevNode, *newNode;

    if (n >= 1)
    {
        /*
         * Creates and links the head node
         */
        head = (struct Node *)malloc(sizeof(struct Node));

        printf("Enter data of 1 node: ");
        scanf("%d", &data);

        head -> data = data;
        head -> next = NULL;

        prevNode = head;

        for (i = 0; i <= n; i++)
        {
            newNode = (struct Node *)malloc(sizeof(struct Node));

            printf("Enter data of %d node: ", i);
            scanf("%d", &data);

            newNode->data = data;
            newNode->next = NULL;

            // Link the previous node with newly created node
            prevNode->next = newNode;

            // Move the previous node ahead
            prevNode = newNode;
        }

        // Link the last node with first node
        prevNode->next = head;

        printf("\nCIRCULAR LINKED LIST CREATED SUCCESSFULLY\n");
    }
}

/**
 * Display the content of the list
 */
void displayList()
{
    struct Node *current;
    int n = 1;

    if (head == NULL)
    {
        printf("List is empty.\n");
    }
    else
    {
        current = head;
        printf("DATA IN THE LIST: \n");

        do
        {
            printf("%d -->> \n", current->data);

            current = current->next;
            n++;
        } while (current != head);
    }
}

void insertAtBeginning(int data)
{
    struct Node *newNode, *current;

    if (head == NULL)
    {
        printf("List is empty.\n");
    }
    else
    {
        /*
         * Creates new node, assign data and links it to head
         */
        newNode = (struct Node *)malloc(sizeof(struct Node));
        newNode->data = data;
        newNode->next = head;

        /*
         * Traverses to last node and links last node
         * with first node which is new node
         */
        current = head;
        while (current->next != head)
        {
            current = current->next;
        }
        current->next = newNode;

        /*Makes new node as head node*/
        head = newNode;

        printf("NODE INSERTED SUCCESSFULLY IN THE BEGINNING\n");
    }
}

void insertAtN(int data, int position)
{
    struct Node *newNode, *current;
    int i;

    if (head == NULL)
    {
        printf("The List is empty.\n");
    }
    else if (position == 1)
    {
        insertAtBeginning(data);
    }
    else
    {
        newNode = (struct Node *)malloc(sizeof(struct Node));
        newNode->data = data;
        /*
         * Traverse to n-1 node
         */
        current = head;
        for (i = 2; i <= position - 1; i++)
        {
            current = current->next;
        }

        /* Links new node with node ahead of it and previous to it*/
        newNode->next = current->next;
        current->next = newNode;

        printf("NODE HAS BEEN INSERTED SUCCESSFULLY.\n");
    }
}