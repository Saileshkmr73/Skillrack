"""
Last Character - Last but one
The program must accept a string S as the input. The program must print the characters from the last but one occurrence of the last character in S. If the last character occurs only once, the program must print -1 as the output.

Boundary Condition(s):
2 <= Length of S <= 100

Input Format:
The first line contains S.

Output Format:
The first line contains the characters from the last but one occurrence of the last character in S or -1.

Example Input/Output 1:
Input:
banana

Output:
ana

Explanation:
The last character in S is a.
The characters from the last but one occurrence of a in S are ana.
So ana is printed as the output.

Example Input/Output 2:
Input:
skillrack

Output:
killrack

Example Input/Output 3:
Input:
enter

Output:
-1


"""

#Your code below
s=input().strip()
start=-1
l=len(s)
for i in range(l-2,-1,-1):
    if s[i]==s[-1]:
        start=i
        break
if (start==-1):
    print("-1")
else:
    print(s[start:])