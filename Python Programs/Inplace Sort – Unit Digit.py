"""
Inplace Sort – Unit Digit:

The program must accept N integers as the input. The program must sort the integers having the same unit digit among N integers in their positions. Then the program must print the N sorted integers as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the N sorted integers based on the given condition.

Example Input/Output 1:
Input:
12
32 78 95 62 42 65 35 95 15 76 46 66

Output:
32 78 15 42 62 35 65 95 95 46 66 76

Explanation:
The integers 32, 62 and 42 have the same unit digit 2. So they are sorted in ascending order in their positions.
The integer 78 remains in the same position as there is only one integer with the unit digit 8.

 

The integers 95, 65, 35, 95 and 15 have the same unit digit 5. So they are sorted in ascending order in their positions.
The integers 76, 46 and 66 have the same unit digit 6. So they are sorted in ascending order in their positions.
Hence the output is
32 78 15 42 62 35 65 95 95 46 66 76

Example Input/Output 2:
Input:
4
50 5180 500 570

Output:
50 500 570 5180

Example Input/Output 3:
Input:
5
98 654 1652 13 1569

Output:
98 654 1652 13 1569

"""

num=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)-1):
    for j in range(i+1,len(l)):
        if l[i]%10==l[j]%10 and l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(*l)