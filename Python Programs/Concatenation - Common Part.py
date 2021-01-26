"""
Concatenation - Common Part
The program must accept a string S and N string values as the input. For each string X among the N string values, the program must compare it with the string S, and print the output based on the following conditions.
- If some characters at end of S are matched with the characters at the begining of X, the program must concatenate the string values S and X so that the common part occurs once.
- If it is possible to concatenate, the program must print the concatenated string as the output. Else the program must print -1 as the output.

Boundary Condition(s):
1 <= Length of S and each string value <= 100
1 <= N <= 50

Input Format:
The first line contains S.
The second line contains N.
The next N lines, each contains a string value.

Output Format:
The first N lines, each contains the concatenated string or -1.

Example Input/Output 1:
Input:
skillrack
5
king
racks
rock
acknowledge
skillrack

Output:
skillracking
skillracks
-1
skillracknowledge
skillrack

Explanation:
Here S = skillrack.
The common part between S and the 1st string is k. So the concatenated string is skillracking, which is printed in the 1st line.
The common part between S and the 2nd string is rack. So the concatenated string is skillracks, which is printed in the 2nd line.
There is no common part between S and the 3rd string. So -1 is printed in the 3rd line.
The common part between S and the 4th string is ack. So the concatenated string is skillracknowledge, which is printed in the 4th line.
The string S and the 5th string are equal. So the string skillrack is printed as it is.

Example Input/Output 2:
Input:
knowledge
7
gender
lodge
ledger
edgeless
edge
dodge
edgeedge

Output:
knowledgender
-1
knowledger
knowledgeless
knowledge
-1
knowledgeedge
"""

#Your code below
S=input().strip()
l=[]
c=0;d=1
n=int(input())
for i in range(n):
    a=input().strip()
    l.append(a)
for i in l:
    g=0
    for j in i:
        if i[c:d]==S[-d:]:
            g=d
        d+=1
    if g==0:
        print("-1")
    else:
        print(S+i[g:])
    d=1