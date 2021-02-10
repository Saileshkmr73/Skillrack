"""
Zig-Zag Swap - Columns
The program must accept an integer matrix of size RxC as the input. The program must modify the matrix by swapping the columns in zig-zag fashion based on the following conditions.
- The first half of the 1st column must be swapped with the second half of the Cth column.
- The second half of the 2nd column must be swapped with the first half of the (C-1)th column.
- The first half of the 3rd column must be swapped with the second half of the (C-2)th column.
- The second half of the 4th column must be swapped with the first half of the (C-3)th column.
- Similarly, the program must swap the remaining columns till (C/2)th column in the matrix.
Finally, the program must print the modified matrix as the output.
Note: The values of R and C are always even.

Boundary Condition(s):
2 <= R, C <= 100

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C integers separated by a space.

Output Format:
The first R lines, each contains C integers separated by a space.

Example Input/Output 1:
Input:
6 6
86 87 66 39 51 28
18 21 62 34 69 89
76 82 35 73 81 86
56 61 36 17 22 53
33 32 71 33 45 31
49 42 17 28 60 10

Output:
53 87 17 39 61 28
31 21 33 34 32 89
10 82 28 73 42 86
56 51 36 66 22 86
33 69 71 62 45 18
49 81 17 35 60 76

Explanation:
Here R = 6 and C = 6.
The integers swapped in the columns are highlighted below.
53 87 17 39 61 28
31 21 33 34 32 89
10 82 28 73 42 86
56 51 36 66 22 86
33 69 71 62 45 18
49 81 17 35 60 76

Example Input/Output 2:
Input:
8 4
49 82 82 86
63 58 42 12
67 32 88 52
55 85 25 15
53 68 32 82
67 55 41 15
18 39 47 19
61 33 12 89

Output:
82 82 68 86
15 58 55 12
19 32 39 52
89 85 33 15
53 82 32 49
67 42 41 63
18 88 47 67
61 25 12 55

Example Input/Output 3:
Input:
4 10
79 49 67 85 90 85 87 19 73 85
10 35 11 43 50 26 17 60 69 10
54 66 35 42 42 40 76 40 45 34
54 80 27 90 11 42 36 32 28 17

Output:
34 49 40 85 40 85 42 19 66 85
17 35 32 43 42 26 90 60 80 10
54 73 35 87 42 90 76 67 45 79
54 69 27 17 11 50 36 11 28 10
"""
R,C=map(int,input().split())
matrix=[list(map(int,input().split())) for row in range(R)]
for row in range(R):
    for col in range(C):
        if col%2==0:
            if row<R//2:
                print(matrix[R//2+row][C-col-1],end=" ")
            else:
                print(matrix[row][col],end=" ")
        else:
            if row<R//2:
                print(matrix[row][col],end=" ")
            else:
                print(matrix[row-R//2][C-col-1],end=" ")
    print()