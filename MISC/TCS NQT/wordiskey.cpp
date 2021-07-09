// #One programming language has the following keywords that cannot be used as identifiers:
// #break, case, continue, default, defer, else, for, func, goto, if, map, range, return, struct, type, var
// #Write a program to find if the given word is a keyword or not

// #Input #1:
// #defer

// #Output:
// #defer is a keyword

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main()
{

    char keywords[16][10] = {"break", "case", "continue", "default", "defer", "else", "for", "func", "goto", "if", "map", "range", "return", "struct", "type", "var"};

    char input[20];

    int flag = 0;
    printf("Enter the keyword: ");
    scanf("%s", input);

    for (int i = 0; i < 16; i++)
    {
        if (strcmp(input, keywords[i]) == 0)
        {
            flag = 1;
            break;
        }
    }

    if (flag == 1)
    {
        printf("%s is a keyword", input);
    }
    else
    {
        printf("%s is not a keyword", input);
    }
}
