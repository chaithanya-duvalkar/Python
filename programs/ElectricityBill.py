'''In this problem, you need to write a program to calculate the electricity bill for a household, based on the units of electricity the household consumed. The price for unit varies based on the slab. The charges per unit for different slabs are as mentioned below:
For the first 50 units (0-50), the charge is 2/unit
For the next 100 units (51-150), the charge is 3/unit
For the next 100 units (151-250), the charge is 5/unit
For above 250 units (251 and above), the charge is 8/ut
Apart from these charges, there is also an additional surcharge of 20% on the total amount is added to the bill.
Input
The input will be a single line containing an integer.
Output
The output should be a single line containing the calculated bill amount.'''

A=int(input())

if A <= 50:
    amounts=A*2
elif A<=150:
    amounts=(50*2)+(A-50)*3
elif A<=250:
    amounts=(50*2)+(100*3)+(A-150)*5 
else:
    amounts=(50*2)+(100*3)+(100*5)+(A-250)*8
total_bill=amounts+(0.20*amounts)
print(total_bill)