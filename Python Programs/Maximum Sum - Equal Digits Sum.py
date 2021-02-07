"""
Maximum Sum - Equal Digits Sum
The program must accept N integers as the input. The program must print the maximum sum of two integers whose digits add up to an equal sum. If there are no such integers, the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 10^8

Input Format:
The first line contains N.
The second line contains N integer values separated by a space.

Output Format:
The first line contains the maximum sum of two integers whose digits add up to an equal sum or -1.

Example Input/Output 1:
Input:
4
15 81 24 36

Output:
117

Explanation:
The sum of digits in 15 is 6.
The sum of digits in 81 is 9.
The sum of digits in 24 is 6.
The sum of digits in 36 is 9.
There are two possible combinations.
15 + 24 = 39.
81 + 36 = 117.
The maximum sum is 117, which is printed as the output.

Example Input/Output 2:
Input:
7
20 3 13 18 9 21 22

Output:
35

Example Input/Output 3:
Input:
5
156 12 49 24 99

Output:
-1
"""
a=int(input())
b,c,max1=list(map(int,input().split())),[],-1
for i in b:
    sum=0
    while i!=0:
        rem=i%10
        i=i//10
        sum=sum+rem
    c.append(sum)
for i in range(0,a):
    for j in range(i+1,a):
        if c[i]==c[j]:
            max1=max(max1,b[i]+b[j])
print(max1)