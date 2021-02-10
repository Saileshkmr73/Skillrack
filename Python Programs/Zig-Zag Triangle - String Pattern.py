"""
Zig-Zag Triangle - String Pattern
The program must accept a string S and an integer N as the input. The program must print N lines of output based on the following conditions.
- The 1st line contains N-1 asterisks and the first character of S.
- The 2nd line contains N-2 asterisks and the next 3 characters of S.
- The 3rd line contains N-3 asterisks and the next 5 characters of S in reverse order.
- The 4th line contains N-4 asterisks and the next 7 characters of S.
- The 5th line contains N-5 asterisks and the next 9 characters of S in reverse order.
- Similarly, the remaining line are printed in the zig-zag order.
- If there are no more characters in S when printing lines, the program must print # for those characters.

Boundary Condition(s):
1 <= Length of S <= 1000
3 <= N <= 50

Input Format:
The first line contains S.
The second line contains N.

Output Format:
The first N lines, each containing the character(s) as per the given condition.

Example Input/Output 1:
Input:
skillrack
3

Output:
**s
*kil
kcarl

Explanation:
S = skillrack
N = 3, so the number of lines to be printed is 3.
In the 1st line, 2 (3-1) asterisks and the first character of S are printed.
In the 2nd line, 1 (3-2) asterisk and the next 3 characters of S are printed.
In the 3rd line, no asterisks (3-3 = 0) and the next 5 characters of S (in reverse order) are printed.
Hence the output is
**s
*kil
kcarl

Example Input/Output 2:
Input:
Telegram
4

Output:
***T
**ele
*#marg
#######

Example Input/Output 3:
Input:
Acknowledgement
3

Output:
**A
*ckn
delwo

"""