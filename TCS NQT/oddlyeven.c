// #Given a maximum of 100 digit numbers as input, find the difference between the sum of odd and even position digits.
// #Input : 9834698765123
// #Expected Output : 1

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void main()
{
    int even = 0, odd = 0, i = 0, n;
    char num[100];

    printf("Enter the number:");
    scanf("%s", num); //get the input up to 100 digit
    n = strlen(num);
    while (n > 0)
    {
        if (i == 0) //add even digits when no of digit is even and vise versa
        {
            even += num[n - 1] - 48;
            n--;
            i = 1;
        }
        else //add odd digits when no of digit is even and vice versa
        {
            odd += num[n - 1] - 48;
            n--;
            i = 0;
        }
    }
    printf("%d", abs(even - odd)); //print the difference of odd and even

}