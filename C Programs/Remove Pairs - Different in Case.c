"""
Remove Pairs - Different in Case
The program must accept a string S as the input. The program must remove two continuous alphabets if they are same but different in case. Similarly, the program must remove the alphabets until there are no two such continuous alphabets in S. If all the characters are removed from the string S, the program must print -1 as the output.

Boundary Condition(s):
2 <= Length of S <= 1000

Input Format:
The first line contains S.

Output Format:
The first line contains the modified string S or -1.

Example Input/Output 1:
Input:
SkilllLRack

Output:
SkillRack

Explanation:
The given string is SkilllLRack.
The continuous alphabets l and L are same but different in case. So they are removed from the string SkilllLRack.
Now, no more such continuous alphabets present in the string. So SkillRack is printed as the output.

Example Input/Output 2:
Input:
CoOcDOOoodjing

Output:
jing

Example Input/Output 3:
Input:
OOOooopPSs

Output:
-1
"""
