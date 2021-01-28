"""
Customers Group - Purchase Amount:

In a pantry, N customers have purchased the items they need. The name of each customer and his/her total purchase amount A are passed as the input to the program. The program must group the customers based on the purchase amount (i.e., the customers with the same purchase amount belong to one group). The program must print the purchase amount and the names of the customers belonging to each group as the output. The purchase amounts must be printed in descending order. In each group, the names of the customers must be printed in sorted order.

Boundary Condition(s):
1 <= N <= 50
1 <= Length of customer's name <= 20
10 <= A <= 10^5

Input Format:
The first line contains N.
The next N lines, each containing the customer name and his/her total purchase amount separated by a space.

Output Format:
The line(s), each containing the total purchase amount and the customer(s) name separated by a space.

Example Input/Output 1:
Input:
5
ghi 1500
def 1200
abc 1500
jkl 1500
mno 1600

Output:
1600 mno
1500 abc, ghi, jkl
1200 def

Explanation:
The purchase amounts in descending order are 1600, 1500 and 1200.
There is only one customer who has purchased the items for 1600.
1600 mno
There are three customers who have purchased the items for 1500.
1500 abc, ghi, jkl
There is only one customer who has purchased the items for 1200.
1200 def

Example Input/Output 2:
Input:
4
abcd 950
Efg 2700
PQR 950
mno 950

Output:
2700 Efg
950 PQR, abcd, mno

"""


n = int(input())
d = {}
for i in range(n):
    name,amnt = input().split(); amnt = int(amnt)
    if amnt not in d.keys(): d[amnt] = [name]
    else: d[amnt].append(name)
l = sorted(d,reverse = 1)
for i in l:
    print(i,end=' ')
    print(*sorted(d[i]),sep=', ')