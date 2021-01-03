"""
Shift Right A
The program must accept a character matrix of size RxC containing only A's and B's as the input. The program must remove all occurrences of B and shift the occurrences of A to the right. The empty cells must be replaced with the hyphens. Then the program must print the modified matrix as the output.

Boundary Condition(s):
2 <= R, C <= 100

Input Format:
The first line contains R and C separated by a space.
The next R lines, each contains C alphabets separated by a space.

Output Format:
The first R lines contain the modified matrix.

Example Input/Output 1:
Input:
4 6
A B A A B B
A A A A A A
B B A A A A
A A A A B A

Output:
- - - A A A
A A A A A A
- - A A A A
- A A A A A

Explanation:
After removing all the occurrences of B, the empty cells are replaced with hyphens.
A - A A - -
A A A A A A
- - A A A A
A A A A - A
After shifting the occurrences of A to the right, the matrix becomes
- - - A A A
A A A A A A
- - A A A A
- A A A A A

Example Input/Output 2:
Input:
5 5
B B A B B 
A B A B A 
A A B B B 
B B A A A 
B B B B A  

Output:
- - - - A
- - A A A
- - - A A
- - A A A
- - - - A

"""
Row,Col=map(int,input().split())
Matrix=[list(map(str,input().split())) for index in range(Row)]
for index in range(Row):
    co=0
    for element in range(Col):
        if(Matrix[index][element]=="A"):
            co+=1 
    print("- "*(Col-co)+"A "*co)
