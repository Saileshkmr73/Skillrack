﻿Sort By Last Name First Name
N persons first and last names are passed as input. The program must sort them based on the last name. If the last names are same, then first name must be taken into account to sort.
Input Format:
The first line contains the value of N.
Next N lines contain the first name and the last name of N persons, with the values separated by a space.
Output Format:
N lines containing the N first and last names separated by a space (sorted by last name, first name)
Boundary Conditions:
2 <= N <= 15
Length of first and last name is between 2 and 50.
Example Input/Output 1:
Input:
7
Arul Prakash
Banu Govind
Abhijit Singh
Syed Siraj
George Joshua
Dhanraj Pillay
Bhagat Singh
Output:
Banu Govind
George Joshua
Dhanraj Pillay
Arul Prakash
Abhijit Singh
Bhagat Singh
Syed Siraj
n=int(input());k=[]
l=[input().strip().split() for i in range(n)]
for i in l:k.append([i[1],i[0]])
k=sorted(k)
for i in k:print(i[1],i[0],sep=' ')
n=int(input());k=[]
l=[input().strip().split() for i in range(n)]
k=[[i[1],i[0]] for i in l];k=sorted(k)
for i in k:print(i[1],i[0],sep=' ')
