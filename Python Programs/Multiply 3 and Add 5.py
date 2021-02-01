"""
Multiply 3 and Add 5
The program must accept an integer N as the input. The program must print YES if it is possible to form the integer N based on the following conditions.
- The initial value must be 3 or 5.
- Then it can be modified using the following two operations.
    Operation 1: Multiply by 3
    Operation 2: Add 5
If it is not possible, the program must print NO as the output.

Boundary Condition(s):
3 <= N <= 10^8

Input Format:
The first line contains N.

Output Format:
The first line contains YES or NO.

Example Input/Output 1:
Input:
19

Output:
YES

Explanation:
Here N = 19.
The only possible way to form 19 is 3 * 3 + 5 + 5.
So YES is printed as the output.

Example Input/Output 2:
Input:
16

Output:
NO
"""

n=int(input())
while n>0:
    if n==5 or n==3:
        print("YES")
        break
    if n%3!=0:
        n-=5
    else:
        n//=3
else:
    print("NO")