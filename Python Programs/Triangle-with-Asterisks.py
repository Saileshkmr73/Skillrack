"""Triangle with Asterisks:

The program must accept a character matrix of size RxC and the positions of the three corners of a triangle (in any order) as the input. The program must replace the characters in the border of the triangle with asterisks. Then the program must print the modified matrix as the output.

Boundary Condition(s):
2 <= R, C <= 50

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C characters separated by a space.
The next three lines from the (R+2)nd line, each contains two integers representing the position of a corner of the triangle.

Output Format:
The first R lines, each contains C characters separated by a space.

Example Input/Output 1:
Input:
8 6
w p H p x u
a G i D x w
C t B m x v
m b g A n B
w g o G t b
n s r G f i
t u w g y z
z u G C z r
4 6
1 3
7 3

Output:
w p * p x u
a G * * x w
C t * m * v
m b * A n *
w g * G * b
n s * * f i
t u * g y z
z u G C z r

Explanation:
The three corners of the triangle in the matrix is highlighted below.
w p H p x u
a G i D x w
C t B m x v
m b g A n B
w g o G t b
n s r G f i
t u w g y z
z u G C z r
After replacing the characters in the border of the triangle with asterisks, the matrix becomes
w p * p x u
a G * * x w
C t * m * v
m b * A n *
w g * G * b
n s * * f i
t u * g y z
z u G C z r

Example Input/Output 2:
Input:
9 10
a k B y j d x k q u
b u C y s z A E B j
x G g z f x x l t D
E t h j D m A A z k
j C E u t x j g j C
E v j i t x s t r w
r p o a m B g o w C
i g h y G s G v t B
f s h w z k b z o E
7 6
4 3
4 6

Output:
a k B y j d x k q u
b u C y s z A E B j
x G g z f x x l t D
E t * * * * A A z k
j C E * t * j g j C
E v j i * * s t r w
r p o a m * g o w C
i g h y G s G v t B
f s h w z k b z o E

"""

