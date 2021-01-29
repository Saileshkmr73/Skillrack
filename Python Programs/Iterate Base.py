"""

Iterate Base – TCS CodeVita: The program must accept a number N in any base from 2 to 36. We can identify the base that would result in a least value for the given representation.

Consider the following examples:
1. For the number representation 11, the least possible base is 2 and hence the least possible value is 3 in base 10.
2. For 17, the least possible base is 8 and the least possible value is 15 in base 10.
3. For 1729, the least possible base in 10 and the least possible value is 1729 in base 10.


 
Consider doing this base reduction iteratively till a fixed point is reached as shown in the following example:
Let’s start with the number representation 72.
The least possible value of 72 is in base 8 and is 58 (represented in base 10).
Iterating, the least possible value of 58 is in base 9 and is 53 (base 10).
In the next iteration, 53 (in base 6) becomes 33.
Then, 33 (base 4) gives 15, 15 (base 6) gives 11, 11 (base 2) gives 3. Finally, 3 remains 3 (in bases 4 and above).

The program must perform the successive base reductions as above and print the resulting final number as the output.

The face values for the symbols are given below.
0 -> 0
1 -> 1
2 -> 2
…
9 -> 9
A -> 10
B -> 11
C -> 12
…
X -> 33
Y -> 34
Z -> 35

Boundary Condition(s):
1 <= Length of N <= 5

Input Format:
The first line contains N.

Output Format:
The first line contains an integer representing the final number representation that results from iteratively performing base reductions in the manner illustrated above.

Example Input/Output 1:
Input:
53

Output:
3

Explanation:
Here N = 53.
53 (base 6) => 33
33 (base 4) => 15
15 (base 6) => 11
11 (base 2) => 3
3 (base 4) => 3, which is the fixed point.
Hence the output is 3

Example Input/Output 2:
Input:
BCD

Output:
679

Explanation:
Here N = BCD.
BCD (base 14) => 2337
2337 (base 8) => 1247
1247 (base 8) => 679
979 (base 10) => 679, which is the fixed point.
Hence the output is 679
"""

def s(a,m):
    sum,l=a[-1],len(a)
    for i in range(l-2,-1,-1):
        sum+=a[i]*m**(l-i-1)
    return [int(i) for i in str(sum)]
a=[ord(i)-(55 if i.isalpha() else 48) for i in input()]
k,c=s(a,max(a)+1),[]
while k!=c:
    c=k
    k=s(k,max(k)+1)
print(*c,sep="")