"""
Sort Integers - Targets
The program must accept N integers and an integer T as the input. The program must print the integers between the first occurring T and the last occurring T in ascending order as the output. If there are no such integers, the program must print -1 as the output.

Boundary Condition(s):
1 <= N <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains T.

Output Format:
The first line contains the integers between the first occurring T and the last occurring T in ascending order or -1.

Example Input/Output 1:
Input:
7
3 2 4 5 4 8 4
4

Output:
4 5 8

Explanation:
Here N = 4.
The integers between the first occurring 4 and last occurring 4 are 5 4 8.
After sorting the integers 5, 4, 8 in ascending order, the integers become 4, 5, 8.
Hence the output is
4 5 8

Example Input/Output 2:
Input:
5
1 8 2 3 4
8

Output:
-1

Example Input/Output 3:
Input:
8
39 11 38 36 29 49 11 16
11

Output:
29 36 38 49
"""

n=int(input())
sortIntegers=list(map(int,input().split()))
t=int(input())
if sortIntegers.count(t)<2 or len(set(sortIntegers))==1:
    print(-1)
else:
    firstInd=sortIntegers.index(t)+1
    lastInd=sortIntegers[::-1].index(t)
    if lastInd==0:
        print(*sorted(sortIntegers[firstInd:-1]))
    else:
        print(*sorted(sortIntegers[firstInd:-lastInd-1]))