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

#include<stdio.h>
#include <stdlib.h>

int main()
{   char a[1001],f=1;
    int l;
    scanf("%s%n",a,&l);
    for(int i=0; i<l-1; i++)
    {   int s=i,e=i+1;
        while(abs(a[s]-a[e])==32&&s>=0&&e<l)
        {   a[s--]=a[e++]=0;
            while(!isalpha(a[s]))
                s--;
        }
        i=e-1;
    }
    for(int i=0; i<l; i++)
    {   if(a[i]!=0)
        {   printf("%c",a[i]);
            f=0;
        }
    }
    if(f)
        printf("-1");
}

