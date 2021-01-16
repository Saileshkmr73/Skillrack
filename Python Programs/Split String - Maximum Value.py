"""
Split String - Maximum Value
The program accept a string S containing only 0s and 1s as the input. The program must split the string S into two substring values so that the concatenation of the number of 0s in the left substring and the number of 1s in the right substring is maximum. Then the program must print those two substring values of S as the output.

Boundary Condition(s):
1 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the two substring values of S as per the given condition.

Example Input/Output 1:
Input:
001110111

Output:
001110 111

Explanation:
Here S = 001110111.
All possible ways to split the string S are given below.
0 01110111 -> 16
00 1110111 -> 26
001 110111 -> 25
0011 10111 -> 24
00111 0111 -> 23
001110 111 -> 33
0011101 11 -> 32
00111011 1 -> 31
The maximum value is 33 (3 zeroes in 001110 & 3 ones in 111).
Hence the output is
001110 111

Example Input/Output 2:
Input:
101010

Output:
1010 10

"""