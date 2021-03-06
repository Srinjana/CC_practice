#include <stdio.h>
#include <stdlib.h>

struct node
{
    int val;
    struct node *next;
};

void print_list(struct node *head)
{
    printf("H->");

    while (head)
    {
        printf("%d->", head->val);
        head = head->next;
    }

    printf("|||\n");
}

void insert_front(struct node **head, int value)
{
    struct node *new_node = NULL;

    new_node = (struct node *)malloc(sizeof(struct node));

    if (new_node == NULL)
    {
        printf("Failed to insert element. Out of memory");
    }

    new_node->val = value;
    new_node->next = *head;

    *head = new_node;
}

void create_loop(struct node *head)
{
    struct node *tmp = head;

    while (tmp->next)
        tmp = tmp->next;

    tmp->next = head->next;
}

void print_loop(struct node *head)
{
    int n = 25;
    printf("H->");

    while (n--)
    {
        printf("%d->", head->val);
        head = head->next;
    }

    printf("|||\n");
}

struct node *detect_loop(struct node *head)
{
    struct node *slow = head;
    struct node *fast = head;

    while (slow && fast->next && fast->next->next)
    {
        fast = fast->next->next;

        if (slow == fast)
        {
            printf("Linked list has a loop.\n");
            return slow;
        }

        slow = slow->next;
    }

    return NULL;
}

void remove_loop(struct node *head, struct node *loop_node)
{
    struct node *near = head;
    struct node *far = head;
    struct node *ptr = loop_node;
    struct node *prev = NULL;

    while (ptr->next != loop_node)
    {
        ptr = ptr->next;
        far = far->next;
    }

    prev = far;
    far = far->next;

    while (near != far)
    {
        prev = far;
        far = far->next;
        near = near->next;
    }

    prev->next = NULL;
}

void detect_and_remove_loop(struct node *head)
{
    struct node *loop_node;

    loop_node = detect_loop(head);

    if (loop_node)
        remove_loop(head, loop_node);
}

void main()
{
    int count = 0, i, val;
    struct node *head = NULL;

    printf("Enter number of elements: ");
    scanf("%d", &count);

    for (i = 0; i < count; i++)
    {
        printf("Enter %dth element: ", i);
        scanf("%d", &val);
        insert_front(&head, val);
    }

    printf("Original List: ");
    print_list(head);
    detect_loop(head);

    printf("Creating loop...\n");
    create_loop(head);
    printf("Printing list with loop");
    print_loop(head);

    printf("Removing loop...\n");
    detect_and_remove_loop(head);

    printf("List after removing loop:\n");
    print_list(head);
}