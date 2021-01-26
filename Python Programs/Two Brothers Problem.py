"""
Two Brothers Problem
There are two brothers (elder & younger) in a family. Both brothers have N children (i.e., total number of children in the entire family). Both brothers own property in terms of cash, gold and land. Also, they have decided to divide their property into their respective children.

The property division rules are given below.
- Divide the cash equally with all children.
- Divide the gold equally with all female children.
- Divide the Land equally with all male children.

The program must accept the values of the cash C (in rupees), the gold G (in grams), the land L (in sq.ft.) for both the brothers as the input. Then the program must accept N non-zero integers representing the N children.
- A positive even integer represents a male child of the elder brother.
- A negative even integer represents a female child of the elder brother.
- A positive odd integer represents a male child of the younger brother.
- A negative odd integer represents a female child of the younger brother.
For each child, the program must print the property values(Cash, Gold and Land) as shown in Example Input/Output section.
Note:
- Each property value must be printed with the precision up to two decimal places.
- Both brothers have at least one male child and one female child.

Boundary Condition(s):
2 <= C, G, L <= 10^8
4 <= N <= 100
-100 <= Each integer value <= 100

Input Format:
The first line contains C, G and L for the elder brother.
The second line contains C, G and L for the younger brother.
The third line contains N.
The fourth line contains N integers separated by a space.

Output Format:
The first N lines, each contains four integers representing the property values based on the given conditions.

Example Input/Output 1:
Input:
10000 200 1000
50000 100 1500
7
10 1 4 -2 -1 2 -7

Output:
10 2500.00 0.00 333.33
1 16666.67 0.00 1500.00
4 2500.00 0.00 333.33
-2 2500.00 200.00 0.00
-1 16666.67 50.00 0.00
2 2500.00 0.00 333.33
-7 16666.67 50.00 0.00

Explanation:
The elder brother has 10000 rupees as cash, 200 grams as gold, and 1000 sq.ft as land.
For the elder brother, there are three male (10, 4 and 2) and one female (-2) children.
The 10000 rupees cash is divided equally with all four children. So each child gets 2500 rupees.
The elder brother has one female child. So one female child gets 200 grams gold.
The 1000 sq.ft. land is divided equally with the three male children. So each male child gets 333.33 sq.ft. land.
The younger brother has 50000 rupees as cash, 100 grams as gold and 1500 sq.ft. as land.
For the younger brother, there are one male (1) and two female (-1 and -7) children.
The 50000 rupees cash is divided equally with all three children. So each child gets 16666.67 rupees.
The 100 grams gold is divided equally with the two female children. So each female child gets 50 grams of gold.
The younger brother has one male child. So one male child gets 1500 sq.ft. land.

Example Input/Output 2:
Input:
34500 1000 1400
15000 550 2000
5
8 -4 3 -9 7

Output:
8 17250.00 0.00 1400.00
-4 17250.00 1000.00 0.00
3 5000.00 0.00 1000.00
-9 5000.00 550.00 0.00
7 5000.00 0.00 1000.00

"""