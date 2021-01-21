"""
Alphabets Triangle Pattern
Given an integer N which indicates the position in the alphabet series (upper case) and another integer R which indicates the number of rows to be printed, the program must print R rows with each row containing alphabets equal to the row count.

Boundary Condition(s):
1 <= N <= 26
1 <= R <= 26

Example Input/Output 1:
Input:
4 5

Output:
D
D E
D E F
D E F G
D E F G H

Explanation:
4 indicates the fourth alphabet which is D.
5 indicates the number of rows to be printed.
Row 1: One alphabet starting from D is printed.
D
Row 2: Two alphabets starting from D are printed.
D E
Row 3: Three alphabets starting from D are printed.
D E F
Row 4: Four alphabets starting from D are printed.
D E F G
Row 5: Five alphabets starting from D are printed.
D E F G H

Example Input/Output 2:
Input:
25 4

Output:
Y
Y Z
Y Z A
Y Z A B

"""


num1,num2=map(int,input().split())
Alpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num1=num1-1
for i in range(num1,num1+num2):
    for j in range(num1,i+1):
        print(Alpha[j%26],end=" ")
    print()