"""
Next Date with Same Weekday

The program must accept a date D in the format DD-MM-YYYY as the input. 
The program must print tne date after 7 days from D (i.e., the oate of tne next weekday of D) as the output.

Boundary Condition(s): 
1 <= DD <= 31
1 <= MM <= 12
1000 <= YYYY <= 2500

Example Input/Output 1: 
Input:
11-08-2020

Output:
18-08-2020

Example Input/Output 2: 
Input:
31-03-2019

Output:
07-04-2019

"""


import datetime
date=input().strip()
date=datetime.datetime.strptime(date,"%d-%m-%Y")
date+=datetime.timedelta(days=7)
print(date.strftime("%d-%m-%Y"))