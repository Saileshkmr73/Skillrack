"""
Christmas Tree Pattern - TCS CodeVita
John is a pure Desi boy. And his one and only dream is to meet Santa Claus. He decided to decorate a Christmas tree for Santa on coming Christmas. John made an interesting Christmas tree that grows day by day.
The Christmas tree is comprised of the following:
- Parts
- Stand
Each Part is further comprised of Branches. 
Branches are comprised of Leaves.
How the tree appears as a function of days should be understood. Basis that print the tree as it appears on the given day. Below are the rules that govern how the tree appears on a given day. Write a program to generate such a Christmas tree whose input is the number of days.
Rules:
1) If the tree is one day old, you cannot grow. Print a message "You cannot generate christmas tree" 
2) Tree will die after 20 days. It should give a message "Tree is no more" 
3) Tree will have one part less than the number of days.
    E.g. On the 2nd day, the tree will have 1 part and one stand.
           On the 3rd day, the tree will have 2 parts and one stand.
           On the 4th day, the tree will have 3 parts and one stand and so on. 
4) Top-most part will be the widest and bottom-most part will be the narrowest. 
5) Difference in number of branches between top-most and second from the top will be 2.
6) Difference in number of branches between second from top and bottom-most part will be 1.
Below is an illustration of how the tree looks like on 4th day


Boundary Condition(s):
1 <= N <= 100
Input Format:
The first line contains the number of days.
Output Format:
The lines contain the Christmas tree or one of the mentioned messages.
Example Input/Output 1:
Input:
4
Output:
----*
---***
--*****
-*******
*********
---***
--*****
-*******
---***
--*****
----*
----*
Example Input/Output 2:
Input:
7
Output:
-------*
------***
-----*****
----*******
---*********
--***********
-*************
***************
------***
-----*****
----*******
---*********
--***********
-*************
------***
-----*****
----*******
---*********
--***********
------***
-----*****
----*******
---*********
------***
-----*****
----*******
------***
-----*****
-------*
-------*

"""

def k(a,k,l):
    for i in range(k,l+1):
        print('-'*(a-i)+'*'*((i+1)*2-1))
a=int(input())
if a==1:
    print('You cannot generate christmas tree')
elif a>20:
    print('Tree is no more')
else:
    k(a,0,a)
    for i in range(1,a-1):
        k(a,1,a-i)
    print(('-'*a+'*'+'\n')*2)


==============================================


n=int(input());a=n
if n<=1:
    print('You cannot generate christmas tree')
elif n>20:
    print('Tree is no more')
else:
    for i in range(1,n+2):
        print("-"*(n-i+1),end='')
        for j in range(-i+1,i):
            print('*',end='')
        print()
    while n!=2:
        for i in range(1,n):
            print('-'*(a-i),end='')
            for j in range(-i-1,i):
                print('*',end='')
            print()
        n-=1
    for i in range(2):
        print('-'*(a),end='')
        for j in range(i,i+1):
            print('*',end='')
        print()

==============================================

n=int(input())
if(n<=1):
    print("You cannot generate christmas tree")
elif(n>20):
    print("Tree is no more")
else:
    for i in range(n+1):
        for j in range(i,n):
            print("-",end="")
        for k in range(2*i+1):
            print("*",end="")
        print()
    if(n>2):
        for s in range(0,n-1):
            for p in range(s,n-1):
                print("-",end="")  
            for q in range((2*(s+2))-1):
                print("*",end="")
            for p in range(s,n-1):
                print(" ",end="")     
            print() 
        for t in range(0,n-3):
            for s in range(n-2):
                for p in range(s,n-1):
                    print("-",end="")   
                for q in range(0,(2*(s+2))-1):
                    print("*",end="")
                for p in range(s,n-1):
                    print(" ",end="")
                print()
        for p in range(0,2):
            for q in range(0,n):
                print("-",end="")
            print("*",end="")
            for q in range(0,n):
                print(" ",end="")
            print()


=====================================================================

n=int(input())
if n<=1:print("You cannot generate christmas tree")
elif n>20:print("Tree is no more")
else:
    for i in range(n+1):
        for j in range(i,n):print("-",end="")
        for k in range((2*i)+1):print("*",end="")
        print()
    if n>2:
        for s in range(n-1):
            for p in range(s,n-1):print("-",end="")  
            for q in range((2*(s+2))-1):print("*",end="")
            for p in range(s,n-1):print(" ",end="")     
            print() 
        for t in range(n-3):
            for s in range(n-2):
                for p in range(s,n-1):print("-",end="")   
                for q in range((2*(s+2))-1):print("*",end="")
                for p in range(s,n-1):print(" ",end="")
                print()
        for p in range(2):
            for q in range(n):print("-",end="")
            print("*",end="")
            for q in range(n):print(" ",end="")
            print()