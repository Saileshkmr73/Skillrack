"""
Maximum Sum Submatrix:

The program must accept an integer matrix of size RxC and an integer K as the input. The program must print the 2x2 submatrix which has the maximum sum among the last K 2x2 non-overlapping submatrices in the matrix. If two or more 2x2 submatrices have the same maximum sum, then the program must print the first occurring submatrix as the output.
Note: The values of R and C are always even.

Boundary Condition(s):
2 <= R, C <= 50
1 <= K <= (R/2)*(C/2)

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.
The (R+2)nd line contains K.

Output Format:
The first two lines, each contains two integers separated by a space.

Example Input/Output 1:
Input:
4 6
7 2 1 7 3 0
8 9 6 4 0 3
2 0 0 8 2 8
8 6 9 5 9 9
4

Output:
2 8
9 9

Explanation:
Here K = 4.
The last 4 2x2 non-overlapping submatrices in the given 4x6 matrix are given below.
3 0
0 3

2 0
8 6

0 8
9 5

2 8
9 9
The last 2x2 submatrix has the maximum sum 28 (2+8+9+9).
Hence the output is
2 8
9 9

Example Input/Output 2:
Input:
4 4
29 77 33 77
39 71 75 34
62 90 35 99
69 85 84 88
4

Output:
62 90
69 85
"""