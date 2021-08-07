// # Sam is an eligible bachelor. He decides to settle down in life and start a family. He goes bride hunting.He wants to marry a girl who has at least one of the 8 qualities mentioned below:-

// # The girl should be rich.
// # The girl should be an Engineer/Doctor.
// # The girl should be beautiful.
// # The girl should be of height 5.3″.
// # The girl should be working in an MNC.
// # The girl should be an extrovert.
// # The girl should not have spectacles.
// # The girl should be kind and honest.
// # He is in search of a bride who has some or all of the 8 qualities mentioned above. On bride hunting, he may find more than one contenders to be his wife.

// # In that case, he wants to choose a girl whose house is closest to his house. Find a bride for Sam who has maximum qualities. If in case, there are more than one contenders who are at equal distance from Sam’’s house; then

// # print ““Polygamy not allowed””.
// # In case there is no suitable girl who fits the criteria then

// # print “”No suitable girl found””
// # Given a Matrix N*M, Sam’s house is at (1, 1). It is denoted by 1. In the same matrix, the location of a marriageable Girl is also denoted by 1. Hence 1 at location (1, 1) should not be considered as the location of a marriageable Girl’s location.

// # The qualities of that girl, as per Sam’’s criteria, have to be decoded from the number of non-zero neighbors (max 8-way) she has. Similar to the condition above, 1 at location (1, 1) should not be considered as the quality of a Girl. See Example section to get a better understanding.

// # Find Sam, a suitable Bride and print the row and column of the bride, and find out the number of qualities that the Bride possesses.

// # NOTE: – Distance is calculated in number of hops in any direction i.e. (Left, Right, Up, Down and Diagonal)

// # Constraints

// # 2 <= N,M <= 10^2
// # Input Format

// # First Line contains the row (N) and column (M) of the houses.
// # Next N lines contain the data about girls and their qualities.
// # Output

// # It will contain the row and column of the bride, and the number of qualities that Bride possess separated by a colon (i.e. :).
// # Explanation

// # Example 1

// # Input:

// # 2 9

// # 1 0 1 1 0 1 1 1 1

// # 0 0 0 1 0 1 0 0 1

// # Output:

// # 1:7:3

// # Explanation:

// # The girl and qualities are present at (1,3),(1,4),(1,6),(1,7),(1,8),(1,9),(2,4),(2,6),(2,9).

// # The girl present at (1,3) has 2 qualities (i.e. (1,4)and (2,4)).
// # The girl present at (1,4) has 2 qualities.
// # The Bride present at (1,6) has 2 qualities.
// # The Bride present at (1,7) has 3 qualities.
// # The Bride present at (1,8) has 3 qualities.
// # The Bride present at (1,9) has 2 qualities.
// # The Bride present at (2,4) has 2 qualities.
// # The Bride present at (2,6) has 2 qualities.
// # The Bride present at (2,9) has 2 qualities.
// # As we see, there are two contenders who have maximum qualities, one is at (1,7) and another at (1,8).
// # The girl who is closest to Sam’s house is at (1,7). Hence, she is the bride.

// # Hence, the output will be 1:7:3.

#include<stdio.h>
int main()
{
    int n, m, i, g[50][50], j, p, q;
    int max = 0, cnt = 0, k = 1, c = 0, u = 1, x[30], y[30], t1, min = 0, sc[50];
    int e, f, ct = 0, a[50], count = 0, t2 = 0, t = 0;
    scanf("% d %d", & n, & m);
    
    for(i=1; i <= n; i++)
    {
        for(j=1; j <= m; j++)
        {
            scanf("% d", & g[i][j]);
        }
    }
    g[1][1] = 0;
    for(i=1; i <= n; i++)
    {
        for(j=1; j <= m; j++)
        {
            cnt = 0;
            if(g[i][j] == 1)
            {
                t++;
                for(p=i-1; p <= i+1; p++)
                {
                    for(q=j-1; q <= j+1; q++)
                    {
                        if(g[p][q] == 1)
                        {
                            cnt++;
                        }
                    }
                }
                cnt = cnt-1;
                a[k] = cnt;
                k++;
            }
        }
    }
    for(k=1; k <= t; k++)
    {
        if(a[k] > max)
        max = a[k];
    }
    if(max == 0)
    {
        printf("No suitable girl found");
        return 0;
    }
    for(k=1; k <= t; k++)
    {
        if(a[k] == max)
        c++;
    }
    for(k=1; k <= t; k++)
    {
        t2 = 0;
        if(a[k] == max)
        {
            for(i=1; i <= n; i++)
            {
                for(j=1; j <= m; j++)
                {
                    if(g[i][j] == 1)
                        t2++;
                    if(t2 == k)
                    {
                        x[u] = i;
                        y[u] = j;
                        u++;
                    }
                }
            }
        }
    }
    t1 = u-1;
    if(c == 1)
        {
            printf("% d: % d: % d", x[1], y[1], max);
        }
    else
    {
        for(u=1; u <= t1; u++)
        {
            sc[u] = sqrt(((x[u]-1) * (x[u]-1)) + ((y[u]-1)*(y[u]-1)));
        }
        min = sc[1];
        for(u=1; u <= t1; u++)
        {
            if(sc[u] < min)
                min = sc[u];
        }
        for(u=1; u <= t1; u++)
        {
            if(sc[u] == min)
                count++;
        }
        if(count > 1)
            printf("Polygamy not allowed");
        if(count == 1)
        {
            for(u=1; u <= t1; u++)
            {
                if(sc[u] == min)
                printf("% d: % d: % d", x[u], y[u], max);
            }
        }

    }
    return 0;
}
