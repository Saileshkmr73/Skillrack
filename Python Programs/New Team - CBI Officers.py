"""
New Team - CBI Officers
There are two CBI teams investigating a case separately. One team contains M officers and other team contains N officers. The program must accept the name and the experience (in years) of each officer in both teams as the input. The government has decided to form a new team of X officers based on the following conditions.
- At least two officers from each team must be included in the new team.
- More experienced officers are preferred than less experienced officers.
- If two or more officers have the same experience, the name must be given priority (ascending order).
The value of X is also passed as the input to the program. The program must print the names of the officers in the new team based on the experience in descending order. If two or more officers have the same experience, then sort those officers based on the name in ascending order.

Boundary Condition(s):
2 <= M, N <= 20
1 <= Length of each officer's name <= 20
1 <= Experience of each officer <= 25
4 <= X <= M+N

Input Format:
The first line contains M.
The next M lines, each contains the name and the experience (in years) of an officer separated by a space.
The (M+2)nd line contains N.
The next N lines from the (M+3)rd line, each contains the name and the experience (in years) of an officer separated by a space.

Output Format:
The first X lines containing the names of the officers in the new team.

Example Input/Output 1:
Input:
4
Abc 2
Bcd 4
Cde 8
Def 5
3
Ghi 3
Efg 1
Fgh 3
6

Output:
Cde
Def
Bcd
Fgh
Ghi
Abc

Explanation:
In the 1st team, there are 4 officers. After sorting the officers based on the given conditions, the names become Cde, Def, Bcd and Abc.
In the 2nd team, there are 3 officers. After sorting the officers based on the given conditions, the names become Fgh, Ghi and Efg.
The size of the new team to be formed is 6.
The officers Cde, Def from the 1st team and the officers Fgh, Ghi from the 2nd team are included in the new team.
The remaining 2 officers (Bcd & Abc) are included and the their names are printed based on the given conditions.
Cde
Def
Bcd
Fgh
Ghi
Abc

Example Input/Output 2:
Input:
3
ABC 7
xyz 5
PQR 5
3
mno 5
Def 5
Stu 5
5

Output:
ABC
Def
PQR
Stu
mno
"""