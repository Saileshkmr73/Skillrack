"""
BINGO Game: 

A Bingo game is played with a 5×5 matrix board. 
When a person correctly guesses a number in the board it is slashed. 
When 5 rows or columns are entirely slashed it is BINGO (As BINGO contains 5 letters).

Given the values for the 5*5 matrix board, 
followed by N numbers which are guesses by a person, 
find the number of guesses needed for a BINGO.

Input format:
First 5 lines each contain 5 numbers with the values for bingo game.
6th line contains N
7th line contains N numbers as guesses by the person separated by space.

Boundary Condition:
1 <= Number in a Bingo board <=50
1 <= Number Guessed <=50

Example Input/Output 1:
Input:
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
33
1 29 2 49 28 3 4 5 47 6 7 8 26 9 11 50 12 27 45 13 16 17 18 21 22 23 24 41 25 36 19 39 42

Output:
29

Explanation:
The guesses required to solve the bingo are
1 29 2 49 28 3 4 5 47 6 7 8 26 9 11 50 12 27 45 13 16 17 18 21 22 23 24 41 25
Last 4 guesses are not required as after 29 guesses the bingo is,
– – – –  –
– – – –  10
– – – 14 15
– – – 19 20
– – – –  –
Here 2 rows and 3 columns are slashed (that is a total of 5 rows or columns are completely slashed)

Code by PSR 🧙‍♂️
"""
a=[]
for i in range(5):
    a.append(list(map(int,input().split())))
n=int(input())
guess=list(map(int,input().split()))
answer=0
for k in range(n):
    val=0
    bingo=0
    for i in range(5):
        for j in range(5):
            if a[i][j]==guess[k]:
                a[i][j]="-"
                val=1
                for m in range(5):
                    if a[m].count("-")==5:
                        bingo+=1 
                    default=0
                    for q in range(5):
                        if a[q][m]=="-":
                            default+=1 
                        else:
                            break
                    if(default==5):
                        bingo+=1 
                break
        if val==1:
            break
    if(bingo>=5):
        answer=k 
        break
print(answer+1)