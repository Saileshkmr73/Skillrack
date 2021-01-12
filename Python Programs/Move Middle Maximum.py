"""
Move Middle Maximum: The program must accept an array of N unique integers (where N is always odd) and an integer T as the input. The program must modify the array T times based on the following conditions.
– Compare the middle three integers (arr[mid-1], arr[mid], arr[mid+1]) and find the maximum value among them.
– If arr[mid-1] is the maximum integer, then it must be moved to the beginning of the array.
– If arr[mid+1] is the maximum integer, then it must be moved to the end of the array.
– If arr[mid] is the maximum integer, then compare the first integer and the last integer in the array, then it must be moved to the side with the maximum value.
Finally, the program must print the integers in the modified array as the output.

Boundary Condition(s):
5 <= N <= 99
1 <= Each integer value <= 10^8
1 <= T <= 100

Input Format:
The first line contains N.
The second line contains N integers separated by a space.
The third line contains T.

Output Format:
The first line contains the integers in the modified array separated by a space.

Example Input/Output 1:
Input:
7
88 3 49 40 80 9 99
4

Output:
49 88 3 9 80 40 99

Explanation:
Here N = 7 and T = 4.
For T = 1, 88 3 49 40 80 9 99 -> 88 3 49 40 9 99 80 (Moved to the end)
For T = 2, 88 3 49 40 9 99 80 -> 49 88 3 40 9 99 80 (Moved to the beginning)

For T = 3, 49 88 3 40 9 99 80 -> 49 88 3 9 99 80 40 (Moved to the end)
For T = 4, 49 88 3 9 99 80 40 -> 49 88 3 9 80 40 99 (Moved to the end)

Example Input/Output 2:
Input:
9
53 79 31 2 43 92 24 73 65
3

Output:
53 79 31 2 24 65 92 43 73

"""

Num=int(input())
array=list(map(int,input().split()))
Temp=int(input())
for ctr in range(1,Temp+1):
    midElements=[array[Num//2-1],array[Num//2],array[Num//2+1]]
    if array[Num//2-1]==max(midElements):
        array.insert(0,array.pop(Num//2-1))
    elif array[Num//2+1]==max(midElements):
        array.append(array.pop(Num//2+1))
    else:
        if array[0]>array[-1]:
            array.insert(0,array.pop(Num//2))
        else:
            array.append(array.pop(Num//2))
print(*array)