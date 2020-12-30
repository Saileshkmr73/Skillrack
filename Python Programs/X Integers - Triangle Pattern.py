"""
X Integers - Triangle Pattern

The program must accept N integers and an integer X as the input. The program must print the integer values in X lines based on the following condition(s).
- The 1st line contains the first integer among the N integers.
- The 2nd line contains the next two integers among the N integers.
- The 3rd line contains the next three integers among the N integers.
- Similarly, the remaining lines contain the integer values.
- The program must consider the N integers circulary to the print the output is X lines.

Boundary Condition(s):
1 <= N, X <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains X.

Output Format:
The first X lines, each containing the integer value(s) separated by a space.

Example Input/Output 1:
Input:
10
83 79 78 66 63 61 54 46 43 16
13

Output:
83
79 78
66 63 61
54 46 43 16
83 79 78 66 63
61 54 46 43 16 83
79 78 66 63 61 54 46
43 16 83 79 78 66 63 61
54 46 43 16 83 79 78 66 63
61 54 46 43 16 83 79 78 66 63
61 54 46 43 16 83 79 78 66 63 61
54 46 43 16 83 79 78 66 63 61 54 46
43 16 83 79 78 66 63 61 54 46 43 16 83

Explanation:
In the 1st line, the first integer 83 is printed.
In the 2nd line, the next two integers 79 and 78 are printed.
In the 3rd line, the next three integers 66, 63 and 61 are printed.
In the 4th line, the next four integers 54, 46, 43 and 16 are printed.
In the 5th line, the first five integers 83, 79, 78, 66 and 63 are printed by considering the 10 integers circularly.
Similarly, the remaining lines contain the integer values.

Example Input/Output 2:
Input:
3
1 2 3
10

Output:
1
2 3
1 2 3
1 2 3 1
2 3 1 2 3
1 2 3 1 2 3
1 2 3 1 2 3 1
2 3 1 2 3 1 2 3
1 2 3 1 2 3 1 2 3
1 2 3 1 2 3 1 2 3 1

"""
Num=int(input())
List=list(map(int,input().split()))
X=int(input())
start=0
for i in range(1,X+1):
    for j in range(start,start+i):
        print(List[j%len(List)],end=" ")
    start=(start+i)%len(List)
    print()