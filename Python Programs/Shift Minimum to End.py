"""
Shift Minimum to End
The program must accept N integers and an integer K as the input. The program must perform the following operation K times in the given N integers.
- Shift the minimum integer between the first two integers to the end.
Finally, the program must print the N modified integers as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 1000
1 <= K <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains K.

Output Format:
The first line contains the N modified integers.

Example Input/Output 1:
Input:
5
29 60 84 26 50
4

Output:
84 29 60 26 50

Explanation:
Here N = 5 and K = 4.
The given 5 integers are 29, 60, 84, 26 and 50.
After the 1st shifting operation, the integers become 60, 84, 26, 50 and 29.
After the 2nd shifting operation, the integers become 84, 26, 50, 29 and 60.
After the 3rd shifting operation, the integers become 84, 50, 29, 60 and 26.
After the 4th shifting operation, the integers become 84, 29, 60, 26 and 50.
Hence the output is
84 29 60 26 50

Example Input/Output 2:
Input:
6
4 5 6 3 2 1
3

Output:
6 2 1 4 5 3

"""

Num=int(input())
Array=list(map(int,input().split()))
for Index in range(1,int(input())+1):
    if Array[0]<Array[1]:
        Array.append(Array.pop(0))
    else:
        Array.append(Array.pop(1))
print(*Array)