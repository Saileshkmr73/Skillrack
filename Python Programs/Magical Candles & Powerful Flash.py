"""
Magical Candles & Powerful Flash
There are N magical candles arranged in a circular fashion where some candles are glowing and some are not. These magical candles never melt but each produce a powerful flash at every X seconds. At each powerful flash of a candle, it illuminates the nearby candles (i.e., the left and right adjacent candles). The program must accept N integers and an integer X as the input. The N integers representing the state of N magical candles. 0 indicates that the candle is not glowing and 1 indicates that the candle is glowing. The program must print the total number of seconds it takes to light all N candles as the output.
Note: Initially, at least one candle is glowing among the N candles.

Boundary Condition(s):
2 <= N <= 1000
1 <= X <= 100

Input Format:
The first line contains N and X separated by a space.
The second line contains N integers separated by a space.

Output Format:
The first line contains the total number of seconds it takes to light all N candles.

Example Input/Output 1:
Input:
9 2
0 1 0 0 1 0 0 0 0

Output:
6

Explanation:
Here N = 9 and X = 2.
For every 2 seconds, the glowing candles illuminates the candles near them (i.e., the left and right adjacent candles of each glowing candle).
It takes 6 seconds to light all 9 candles.
At t = 1, 0 1 0 0 1 0 0 0 0
At t = 2, 1 1 1 1 1 1 0 0 0
At t = 3, 1 1 1 1 1 1 0 0 0
At t = 4, 1 1 1 1 1 1 1 0 1
At t = 5, 1 1 1 1 1 1 1 0 1
At t = 6, 1 1 1 1 1 1 1 1 1
So 6 is printed as the output.

Example Input/Output 2:
Input:
10 7
0 0 1 0 0 1 0 0 0 0

Output:
21

"""

