"""
Maximum Difference - Subsequent Integers
The program must accept N integers as the input. The program must sort the N integers and print the maximum difference between the subsequent integers as the output.

Boundary Condition(s):
2 <= N <= 100
1 <= Each integer value <= 10^5

Input Format:
The first line contains N.
The second line contains N integers separated by a space.

Output Format:
The first line contains an integer representing the maximum difference between the subsequent integers after sorting the given N integers.

Example Input/Output 1:
Input:
6
5 9 3 6 4 8

Output:
2

Explanation:
The 6 integers are 5 9 3 6 4 8.
After sorting the integers, the integers become 3, 4, 5, 6 and 8.
The difference between 3 and 4 is 1.
The difference between 4 and 5 is 1.
The difference between 5 and 6 is 1.
The difference between 6 and 8 is 2.
The difference between 8 and 9 is 1.
So the maximum difference between the subsequent integers is 2, which is printed as the output.

Example Input/Output 2:
Input:
7
88 12 49 10 49 63 53

Output:
37


"""
n = input()
a=sorted(map(int, input().split()))
print(max(abs(x-y) for x,y in zip(a,a[1:])))