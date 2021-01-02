"""
Longest String - Vertically/Horizontally
The program must accept a character matrix of size RxC and the position of a cell (X, Y) as the input. The program must form four string values based on the following conditions.
- The string S1 must be formed by traversing the cells from the given cell vertically towards top.
- The string S2 must be formed by traversing the cells from the given cell horizontally towards right.
- The string S3 must be formed by traversing the cells from the given cell vertically towards bottom.
- The string S4 must be formed by traversing the cells from the given cell horizontally towards left.
Finally, the program must print the longest string among the four string values as the output. If two or more string values have the same maximum length, the program must print the first occurring string as the output.
Boundary Condition(s):
2 <= R, C <= 50
1 <= X <= R
1 <= Y <= C
Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The (R+2)nd line contains X and Y separated by a space.
Output Format:
The first line contains the longest string among the four string values.
Example Input/Output 1:
Input:
7 6
s C G o f a
w j o t F i
b j f g k t
k G p j E p
f y w r r G
B m h h g m
e y w b m k
3 3
Output:
fpwhw
Explanation:
The position of the given cell is (3, 3).
S1 = foG.
S2 = fgkt.
S3 = fpwhw.
S4 = fjb.
The string fpwhw is the longest string. So it is printed as the output.
Example Input/Output 2:
Input:
9 5
o u w t f
a B g b D
l o k a r
x w F m C
i d k p w
j f r k p
c v x e a
o w o d E
y o b g G
5 2
Output:
dwoBu
"""

ROW,COL = map(int,input().split())
MATRIX = [input().split() for element in range(ROW)]
X,Y = map(int,input().split())
X,Y = X-1,Y-1
A1,A2,A3,A4 = '','','',''
for index in range(X,-1,-1):
    A1 += MATRIX[index][Y]
for index2 in range(Y,COL):
    A2 += MATRIX[X][index2]
for index in range(X,ROW):
    A3 += MATRIX[index][Y]
for index2 in range(Y,-1,-1):
    A4 += MATRIX[X][index2]
print(max([A1,A2,A3,A4],key = len))