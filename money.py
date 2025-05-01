
'''

'''



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

'''

'''

A=int(input())

five_hundreds=int(A/500)
a=A-(500*five_hundreds)
fiftys=int(a/50)
b=a-(50*fiftys)
tens=int(b/10)
c=b-(10*tens)
ones=int(c/1)

print("500:",five_hundreds,"50:",fiftys,"10:",tens,"1:",ones)