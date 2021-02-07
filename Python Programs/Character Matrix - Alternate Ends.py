"""
Character Matrix - Alternate Ends
The program must accept a character matrix of size RxC as the input. The program must print the output based on the following conditions.
- The first character in the 1st row of the matrix must be printed in the 1st line.
- The last 2 characters in the 2nd row of the matrix must be printed in the 2nd line.
- The first 3 characters in the 3rd row of the matrix must be printed in the 3rd line.
- The last 4 characters in the 4th row of the matrix must be printed in the 4th line.
- Similarly, the program must print the characters of the matrix in the remaining lines as the output.

Boundary Condition(s):
2 <= R, C <= 100

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.

Output Format:
The first R lines contain the characters based on the given conditions.

Example Input/Output 1:
Input:
6 6
a b c d e f
g h i j k l
m n o p q r
s t u v w x
y z a b c d
e f g h i j

Output:
a
kl
mno
uvwx
yzabc
efghij

Explanation:
The first character in the 1st row is a.
The last 2 characters in the 2nd row are k and l.
The first 3 characters in the 3rd row are m, n and o.
The last 4 characters in the 4th row are u, v, w and x.
The first 5 characters in the 5th row are y, z, a, b and c.
The last 6 characters in the 6th row are e, f, g, h, i and j.
Hence the output is 
a
kl
mno
uvwx
yzabc
efghij

Example Input/Output 2:
Input:
8 5
v f b z c
w o j E a
o F f b k
s o f x l
v n i n C
o u r r B
c p w E x
E r b l o

Output:
v
Ea
oFf
ofxl
vninC
ourrB
cpwEx
Erblo

"""