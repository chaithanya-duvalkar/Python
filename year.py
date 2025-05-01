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


A=int(input())

hundreds=int(A/100)
a=A-(100*hundreds)
fiftys=int(a/50)
b=a-(50*fiftys)
tens=int(b/10)
c=b-(10*tens)
ones=int(c/1)

print(f"100:{hundreds}")
print(f"50:{fiftys}")
print(f"10:{tens}")
print(f"1:{ones}")
