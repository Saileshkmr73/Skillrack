﻿Equidistant Characters from Start & End
Equidistant Characters from Start & End: Given a string value S1 the program must print only the characters which are present in the same position from the start of S1 as well as the end of S1 in the order of their occurrence.
Boundary Condition(s):
1 <= Length of S1 <= 1000
Input Format:
The first line contains S1.
Output Format:
The first line contains the string value containing the characters which are present in the same position from the start of S1 as well as the end of S1.
Example Input/Output 1:
Input:
engine
Output:
en
Example Input/Output 2:
Input:
malayalam
Output:
malay
Program:
#include<stdio.h>
 #include <stdlib.h>

int main()
 {
 char str1[1000];
 int i,j;
 scanf("%s",str1);
 int len=strlen(str1);
 for(i=0,j=len-1;i<=len/2,j>=len/2;i++,j--)
 {
 if(str1[i]==str1[j])
 {
 printf("%c",str1[i]);
 }
 }

}
