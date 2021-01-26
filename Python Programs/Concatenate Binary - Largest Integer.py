"""
Concatenate Binary - Largest Integer
The program must accept two integers X and Y as the input. The program must print the largest possible integer which is formed by concatenating the binary representations of X and Y as the output.

Boundary Condition(s):
1 <= X, Y <= 10^4

Input Format:
The first line contains X and Y separated by a space.

Output Format:
The first line contains the largest possible integer which is formed by concatenating the binary representations of X and Y.

Example Input/Output 1:
Input:
7 10

Output:
122

Explanation:
The binary representation of 7 is 111.
The binary representation of 10 is 1010.
The largest possible integer formed is 122 and its binary representation is 1111010.
So 122 is printed as the output.

Example Input/Output 2:
Input:
8 5

Output:
88
"""

num1,num2=map(int,input().split())
bin1=bin(num1)[2:]
bin2=bin(num2)[2:]
x=int(bin1+bin2,2)
y=int(bin2+bin1,2)
if x>y:
    print(x)
else:
    print(y)