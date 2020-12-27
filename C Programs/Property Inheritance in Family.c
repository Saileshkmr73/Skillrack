/*
Property Inheritance in Family:

The hierarchy of a family is given as the input. 
The first N lines contain the family hierarchy with each line containing the parent and the child names separated by a space.
Each person in the family inherits the property only from his parent.
(The value of the property of a parent is divided equally among his children).

After the family hierarchy information, the names of two family members X & Y are also passed as the input. 
The value of property V inherited by the family member X is also given as the input.

The program must find and print the value of property inherited by the family member Y.

Note: If the value of the property of a parent cannot be divided by the number of children without leaving a remainder, then consider the floor value as the amount inherited by a single child. (As an example if the property worth is 10000 and number of children is 3, then the amount inherited by a single child is 3333).

Boundary Condition(s):
1 <= N <= 50
1 <= Length of name of a family member <= 100
0 < V <= 999999999

Input Format:
The first line contains N.
The next N lines contain the name of parent and child names in each line separated by space(s).
The (N+2)th line contains X and V separated by space(s).
The (N+3)th line contains Y.


 
Output Format:
The first line contains the value of property inherited by Y.

Example Input/Output 1:
Input:
6
Ram Ragu
Ram Dheeran
Ragu Vimal
Dheeran Kamal
Dheeran Lokesh
Dheeran Sabari
Lokesh 10000
Ragu

Output:
30000

Explanation:
The family hierarchy is as given below.
Ram
 – Ragu
    – Vimal
 – Dheeran
    – Kamal
    – Lokesh
    – Sabari
Lokesh inherits 10000. Hence amount inherited by Dheeran is 3*10000 = 30000 (As 3 children).
As Ragu and Dheeran are siblings, Ragu also inherits 30000.

Example Input/Output 2:
Input:
8
Kamal Laxman
Laxman Maaran
Maaran Dilip
Maaran Kumar
Dilip Sanjay
Kumar Magesh
Sanjay Harish
Sanjay Kishore
Harish 2500
Magesh

Output:
5000
*/

#include<stdio.h>

#include <stdlib.h>

int v(char a[][2][101], char * b, int n) {
    int x = 1, j = -1, k = 0;
    while (1) {
        for (int i = 0; i < n; i++) {
            if (strcmp( & a[i][1], b) == 0) {
                j = i;
                break;
            }
        }
        if (j == -1)
            return x;
        for (int i = 0; i < n; i++)
            k += (strcmp( & a[i][0], & a[j][0]) == 0);
        x *= k;
        strcpy(b, & a[j][0]);
        k = 0;
        j = -1;
    }
}
int main() {
    int n, k = 0, x;
    scanf("%d", & n);
    char a[n][2][101], b[101], c[101];
    for (int i = 0; i < n; i++)
        scanf("%s %s ", a[i][0], a[i][1]);
    scanf("%s %d %s ", b, & x, c);
    x *= v(a, b, n);
    x /= v(a, c, n);
    printf("%d ", x);
}
