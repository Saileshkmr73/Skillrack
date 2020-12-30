"""
Swap Subsets - Sum

The program must accept N integers as the input. The program must swap every two subsets of size 3 among the N integers. Then the program must print the sum of every two integers as the output.
Note: The value of N is always a multiple of 6.

Boundary Condition(s):
6 <= N <= 996
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains N/2 integers based on the given conditions.

Example Input/Output 1:
Input:
12
2 7 4 15 5 9 11 10 6 12 14 1

Output:
20 11 11 26 12 16

Explanation:
The given 12 integers are 2 7 4 15 5 9 11 10 6 12 14 1.
After swapping every two subsets of size 3, the integers become 15 5 9 2 7 4 12 14 1 11 10 6.
The sum of 15 and 5 is 20.
The sum of 9 and 2 is 11.
The sum of 7 and 4 is 11.
The sum of 12 and 14 is 26.
The sum of 1 and 11 is 12.
The sum of 10 and 6 is 16.
Hence the output is
20 11 11 26 12 16

Example Input/Output 2:
Input:
6
14 8 15 3 10 1

Output:
13 15 23
"""

n=int(input())
a=list(map(int,input().split()))
for i in range(0,n,6):
    a[i:i+3],a[i+3:i+6]=a[i+3:i+6],a[i:i+3]
for i in range(0,n,2):
    print(a[i]+a[i+1],end=" ")