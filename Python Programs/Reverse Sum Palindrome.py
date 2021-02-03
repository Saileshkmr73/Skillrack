"""
Reverse Sum Palindrome
The program must accept an integer N as the input. The program must find the sum of N and its reverse. The program must print the sum if it is a palindromic integer. Else the program must print the next largest palindromic integer of the sum as the output.

Boundary Condition(s):
2 <= N <= 10^7

Input Format:
The first line contains N.

Output Format:
The first line contains an integer based on the given conditions.

Example Input/Output 1:
Input:
12

Output:
33

Explanation:
Here N = 12.
The sum of 12 and its reverse 21 is 33 which is a palindromic integer.
So 33 is printed as the output.

Example Input/Output 2:
Input:
8

Output:
22

Explanation:
Here N = 8.
The sum of 8 and its reverse 8 is 16 which is NOT a palindromic integer.
So the next largest palindromic integer 16 is 22, which is printed as the output.
"""
s=input().strip()
b=s[::-1]
c=int(s)+int(b)
if str(c)==str(c)[::-1]:print(c)
else:
    for i in range(c+1,1000000000):
        if str(i)==str(i)[::-1]:
            print(i)
            exit()