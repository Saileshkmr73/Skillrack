"""
Dragons & Bombs
There are D dragons in a video game, where each dragon has its life denoted by an integer. If the life of a dragon is 0, it means it is dead. The player has the option to kill the dragons by dropping bombs on them. Each bomb has a capacity X and it reduces the life of each dragon by X. If the life of a dragon goes below 0 when a bomb is dropped, the player will lose his life and the game ends.
The program must accept D integers representing the lives of D dragons as the input. Then the program must accept B integers representing the capacities of B bombs. After dropping each bomb, the program must print the lives of the D dragons as the output. Finally, the program must print the string value "Game Over".

Boundary Condition(s):
1 <= D, B <= 100
1 <= Life of each dragon, Capacity of each bomb <= 10^5

Input Format:
The first line contains D.
The second line contains D integers representing the lives of D dragons separated by a space.
The third line contains X.
The fourth line contains X integers representing the capacities of B bombs separated by a space.

Output Format:
The lines, each containing the lives of the D dragons after dropping a bomb.
The last line contains a string value "Game Over".

Example Input/Output 1:
Input:
5
6 5 5 6 5
4
3 1 1 1

Output:
3 2 2 3 2
2 1 1 2 1
1 0 0 1 0
Game Over

Explanation:
The lives of 5 dragons are 6 5 5 6 5.
B = 1 -> (X = 3) 3 2 2 3 2
B = 2 -> (X = 1) 2 1 1 2 1
B = 3 -> (X = 1) 1 0 0 1 0
B = 4 -> (X = 1) The player loses his life and the game ends, so Game Over is printed.

Example Input/Output 2:
Input:
4
3 5 3 3
3
1 1 1

Output:
2 4 2 2
1 3 1 1
0 2 0 0
Game Over

Example Input/Output 3:
Input:
6
7 7 6 9 8 5
6
3 1 3 8 2 9

Output:
4 4 3 6 5 2
3 3 2 5 4 1
Game Over

Explanation:
The lives of 6 dragons are 7 7 6 9 8 5.
B = 1 -> (X = 3) 4 4 3 6 5 2
B = 2 -> (X = 1) 3 3 2 5 4 1
B = 3 -> (X = 3) The player loses his life and the game ends (the life of the 3rd dragon and 6th dragon goes below 0), so Game Over is printed.
"""
d=int(input())
a=list(map(int,input().split()))
x=int(input())
b=list(map(int,input().split()))
i=0
lose=0
while i!=x:
    for j in range(d):
        a[j]-=b[i]
        if a[j]<0:
            lose=1
    if lose:
        break
    print(*a)
    i+=1
print("Game Over")