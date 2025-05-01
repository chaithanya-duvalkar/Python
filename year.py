'''
Given N number of days as input, write a program to convert N number of days to years (Y),
weeks(W) and days(D).
'''
N=int(input())

Y=N//365
remaining_days=N%365

W=remaining_days//7
D=remaining_days%7

print(Y)
print(W)
print(D)

