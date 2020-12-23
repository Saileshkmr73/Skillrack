﻿Basket with Most Colors
There are N trees in straight line. The trees have different colors of flowers. Each color is represented by an alphabet. N strings are passed as input each representing the colors of the flower of the tree. There is a basket under every tree numbered from 1 to N. The flowers fall under the basket directly under its tree and also the basket under the trees adjacent to it. The program must find the basket having the most number of different colors of flowers in it and print its number.
Note:
If more than one basket has the most number of different colors of flower print the first occurring the basket number.
The strings can consist of upper case letters from 'A' to 'Z'.
Boundary Condition(s):
2 <= N <= 1000 
1 <= Length of string <= 100
Input Format:
The first line contains N.
The second line contains N strings separated by space(s).
Output Format:
The first line contains the number of the basket having the most number of different colors of flowers.
Example Input/Output 1:
Input:
3
R GG BG
Output:
2
Explanation:
The basked under the first tree contains two colors of flowers R and G.
The basked under the second tree contains three colors of flowers R, G and B.
The basked under the last tree contains two colors of flowers B and G.
Example Input/Output 2:
Input:
5
RRGV G YYGG VIBGO GR
Output:
4
Explanation:
The basket under the fourth tree has 7 colors of flowers in it. Four colors (VIBGO) of flowers from the tree in the same position. Two colors of flowers (Y and R) from the trees adjacent to it.
import java.util.*;
public class Hello {

    public static void main(String[] args) {
        Map<Integer,HashSet<Character>> map=new HashMap<>();
        Scanner scan=new Scanner(System.in);
        int num=scan.nextInt();
        scan.nextLine();
        String[] strin=scan.nextLine().split(" ");
        
        for(int ele=1;ele<=num;ele++){
            String str=strin[ele-1];
            if(!map.containsKey(ele))map.put(ele,new HashSet<Character>());
            if(ele>1 && ele<num){
                map.put(ele+1,new HashSet<Character>());
                for(char ch:str.toCharArray()){
                    map.get(ele-1).add(ch);
                    map.get(ele).add(ch);
                    map.get(ele+1).add(ch);
                }
            }
            else if(ele==1){
                map.put(ele+1,new HashSet<Character>());
                for(char ch:str.toCharArray()){
                    map.get(ele).add(ch);
                    map.get(ele+1).add(ch);
                }
            }
            else{
                for(char ch:str.toCharArray()){
                    map.get(ele).add(ch);
                    map.get(ele-1).add(ch);
                }
            }
        }
        int max=map.get(1).size(),pos=1;
        for(int ele=1;ele<=num;ele++){
            int temp=map.get(ele).size();
            if(temp > max ){
                max=temp;
                pos=ele;
            }
        }
        System.out.print(pos);
	}
}
