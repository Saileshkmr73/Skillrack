﻿Range Start and End Position
Range Start and End Position: N integers are passed as input. X which is an integer is also passed as the input. The program must print the start S and end E positions of X in these N integers. -1 must be printed as the start and end positions when X is not present in these N numbers.
Input Format:The first line contains N. The second line contains N integer values separated by a space. The third line contains X.
Output Format:The first line contains S and E separated by a space.
Boundary Conditions:2 <= N <= 1000 -9999 <= X <= 9999
Example Input/Output 1:
Input:
5
1 2 3 1 3 3
Output:
3 5
Example Input/Output 2:
Input:
7
10 20 10 20 30 40 50 60
Output:
-1 -1
n=int(input())
a=[int(i) for i in input().split()]
m=int(input())
x,y=-1,-1
for i in range(n):
    if m == a[i]:
        x = i+1 if x==-1 else x
        y = i+1
print(x,y)
