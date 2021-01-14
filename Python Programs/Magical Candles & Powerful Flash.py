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

Code in Python:

Num,Temp=map(int,input().split())
Array=list(map(int,input().split()))
for element in range(Temp,1001,Temp):
    newArray=[0]*Num
    for index in range(Num):
        if Array[index]==1:
            newArray[index]=1
            newArray[(index-1)%Num]=1
            newArray[(index+1)%Num]=1
    Array=newArray
    for i in Array:
        if i==0:
            break
    else:
        print(element)
        break



Code in C:
   

#include<stdio.h>

#include <stdlib.h>

int main() {
    int n, s, f = 0, ma = 0, m = 0, k = -1;
    scanf("%d%d", & n, & s);
    char a[n];
    for (int i = 0; i < n; i++) {
        scanf("%d", & a[i]);
        if (a[i] == 0) m = 1;
        if (k == -1 && a[i]) k = i;
    }
    if (m) {
        for (int i = k + 1; i != (k - 1 == -1 ? n - 1 : k - 1); i = (i + 1) % n) {
            if (a[(i == n - 1 ? 0 : i + 1)] || a[(i == 0 ? n - 1 : i - 1)]) {
                ma = ma < f ? f : ma;
                f = 0;
            } else
                f++;
        }
        ma = ma < f ? f : ma;
    }
    m += (ma / 2) + (ma & 1);
    printf("%d", s * m);
}

