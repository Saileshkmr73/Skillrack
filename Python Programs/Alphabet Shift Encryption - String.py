"""
Alphabet Shift Encryption - String
The program must accept a string S containing only alphabets and L integers as the input (where L is the length of S). For each integer X among the L integers, the program must encrypt the first P alphabets in the string, where P represents the position of the integer X. To encrypt an alphabet, the alphabet must be replaced by the following Xth alphabet with the same case in the English alphabet set. Finally, the program must print the modified string S as the output.
Note: The English alphabet set must be considered in a cyclic fashion for finding the Xth alphabet in the encryption.

Boundary Condition(s):
1 <= Length of S <= 100
1 <= Each integer value <= 1000

Input Format:
The first line contains S.
The second line contains L integers separated by a space.

Output Format:
The first line contains the modified string S.

Example Input/Output 1:
Input:
big
2 1 6

Output:
kpm

Explanation:
Here S = big.
The length of S is 3 and the three integers are 2, 1 and 6.
X = 2 -> After encrypting the first alphabet, the string becomes dig.
X = 1 -> After encrypting the first 2 alphabets, the string becomes ejg.
X = 6 -> After encrypting the first 3 alphabets, the string becomes kpm.
So kpm is printed as the output.

Example Input/Output 2:
Input:
SkillRack
8 7 6 5 3 2 1 4 9

Output:
LvmjeHopt

"""

s=list(input().strip())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    for j in range(0,i+1):
        for k in range(1,l[i]+1):
            a=ord(s[j])+1
            if a==123 or a==91:
                a-=26
            s[j]=chr(a)
print(''.join(s))