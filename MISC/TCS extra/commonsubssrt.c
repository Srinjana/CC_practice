// Today we will learn program to count common subsequence in two strings.We will take two strings as an input, then we will 2 - D ”cnt[][]” array that will store the count of common subsequence found.Now we will iterate each character of first string and each character of second string from of the string to its end, then if the characters matches we will check if the previous character of both string are same or not if they are same we will assign ”1 + cnt[i][j – 1] + cnt[i – 1][j]” to our 2D else we will assign ”cnt[i][j – 1] + cnt[i – 1][j] – cnt[i – 1][j – 1]” to our 2D array.As the iteration ends we will get our count.

#include <stdio.h>
#include <string.h>

int countsequences(char str[], char str2[])
{
    int n1 = strlen(str);
    int n2 = strlen(str2);
    int cnt[n1 + 1][n2 + 1];
    
    for (int i = 0; i <= n1; i++)
    {
        for (int j = 0; j <= n2; j++)
        {
            cnt[i][j] = 0;
        }
    }
    //Taking each character from first string.
    for (int i = 1; i <= n1; i++)
    {
        //Taking each character from second string.
        for (int j = 1; j <= n2; j++)
        {
            //If characters are same in both the string.

            if (str[i - 1] == str2[j - 1])
            {
                cnt[i][j] = 1 + cnt[i][j - 1] + cnt[i - 1][j];
            }
            else
            {
                cnt[i][j] = cnt[i][j - 1] + cnt[i - 1][j] - cnt[i - 1][j - 1];
            }
        }
    }
    return cnt[n1][n2];
}

int main()
{
    char str[100], str2[100];
    printf("Enter the first string: ");
    gets(str);
    printf("Enter string second: ");
    gets(str2);
    printf("Number of common subsequence is: %d ", countsequences(str, str2));
    return 0;
}
