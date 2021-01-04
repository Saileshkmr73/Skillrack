"""
Four Digit Integers Divisible
The program must accept a string S containing only digits and an integer K as the input. The program must print the number of four-digit integers divisible by K which are formed using the substrings of S.
Note: The four-digit integers must not have leading zeroes.

Boundary Condition(s):
4 <= Length of S <= 100
1 <= K <= 1000

Input Format:
The first line contains S.
The second line contains K.

Output Format:
The first line contains an integer representing the number of four-digit integers divisible by K which are formed using the substrings of S.

Example Input/Output 1:
Input:
4287452036
5

Output:
2

Explanation:
Here S = 4287452036 and K = 5.
The four-digit integers divisible by 5 are 8745 and 4520, which are the substrings of S.
So their count 2 is printed as the output.

Example Input/Output 2:
Input:
53200180
12

Output:
0

"""

String=input().strip()
K=int(input())
Count=0
List=[]
for ele in range(len(String)-3):
    if int(String[ele:ele+4])%K==0 and String[ele]!='0':
        List.append(int(String[ele:ele+4]))
        
print(len(List))