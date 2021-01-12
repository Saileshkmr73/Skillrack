"""
Fill Water Tanks - Rain
There are N water tanks arranged in a row. The maximum capacity of each water tank is passed as the input to the program. The initial amount of water in each tank is also passed as the input to the program. If it rains over the N tanks for an hour, 1 litre of water will be filled in each tank. The program must print the total amount of water that has overflowed from the tanks when all the N tanks are completely filled with water.

Boundary Condition(s):
2 <= N <= 100
1 <= Maximum capacity of each water tank <= 1000
0 <= Initial amount of water in each tank <= 1000

Input Format:
The first line contains N.
The second line contains N integers representing the maximum capacity of the N tanks.
The third line contains N integers representing the initial amount of water in the N tanks.

Output Format:
The first line contains the total amount of water that has overflowed from the tanks when all the N tanks are completely filled with water.

Example Input/Output 1:
Input:
4
10 20 15 10
8 15 12 6

Output:
6

Explanation:
The maximum capacity of the 4 tanks are given below.
10 20 15 10
Initially, the amount of water in the 4 tanks are given below.
8 15 12 6
After 1 hour of rain, the amount of water in the 4 tanks are given below.
9 16 13 7 (No overflow)
After 2 hours of rain, the amount of water in the 4 tanks are given below.
10 17 14 8 (No overflow)
After 3 hours of rain, the amount of water in the 4 tanks are given below.
10 18 15 9 (Total overflowed - 1 litre)
After 4 hours of rain, the amount of water in the 4 tanks are given below.
10 19 15 10 (Total overflowed - 3 litres)
After 5 hours of rain, the amount of water in the 4 tanks are given below.
10 20 15 10 (Total overflowed - 6 litres)

Example Input/Output 2:
Input:
6 
15 9 8 13 11 7
14 6 4 11 10 7

Output:
13

"""
Num=int(input())
list_A=list(map(int,input().split()))
list_B=list(map(int,input().split()))
array=[index[0]-index[1] for index in zip(list_A,list_B)]
k=max(array)
array=[k-index for index in array]
print(sum(array))
