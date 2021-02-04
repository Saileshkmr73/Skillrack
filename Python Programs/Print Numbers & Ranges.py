"""
Print Numbers & Ranges
The program must accept N unique integers as the input. The program must print the integers and the integer ranges present in the given N integers in sorted order separated by a comma as the output. The integer range must be represented by the starting value and the ending value separated by a hyphen.

Boundary Condition(s):
2 <= N <= 100
0 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains the integers and the integer ranges separated by a comma.

Example Input/Output 1:
Input:
10
1 0 25 24 3 45 2 15 4 6

Output:
0-4,6,15,24-25,45

Explanation:
Here N = 10 and the 10 integers are 1 0 25 24 3 45 2 15 4 6.
The integers in the range 0-4 are present in the given 10 integers.
The integer 6 is present in the given 10 integers.
The integer 15 is present in the given 10 integers.
The integers in the range 24-25 are present in the given 10 integers.
The integer 45 is present in the given 10 integers.
So they are printed in ascending order as the output.
0-4,6,15,24-25,45

Example Input/Output 2:
Input:
5
1 3 4 6 5

Output:
1,3-6
"""
