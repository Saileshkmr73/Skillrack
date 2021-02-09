"""
Swap Two Characters & Compare
The program must accept two string values S1 and S2 of equal length as the input. The program must check if S1 is equal to S2 by swapping any two characters in S1. If it is possible to make S1 equals to S2, then the program must print YES as the output. Else the program must print NO as the output.
Note: S1 and S2 are always not equal.

Boundary Condition(s):
2 <= Length of S1, S2 <= 1000

Input Format:
The first line contains S1.
The second line contains S2.

Output Format:
The first line contains either YES or NO.

Example Input/Output 1:
Input:
abcd
adcb

Output:
YES

Explanation:
S1 = abcd and S2 = adcb.
After swapping the two characters b and d in the string abcd, the string becomes adcb.
Now both S1 and S2 are equal.
So YES is printed as the output.

Example Input/Output 2:
Input:
skillrack
asillrkck

Output:
NO

Example Input/Output 3:
Input:
ElephantEagle
ElephantBogle

Output:
NO


"""
a=list(input().strip())
b=list(input().strip())
l=len(a)
for i in range(l):
    for j in range(i+1,l):
        a[i],a[j]=a[j],a[i]
        if(a==b):
            print("YES")
            exit()
        a[i],a[j]=a[j],a[i]
        
print("NO")